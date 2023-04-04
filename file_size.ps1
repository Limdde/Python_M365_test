$UPN ="admin@M365x45813228.onmicrosoft.com" 

Connect-MgGraph -Scopes "Mail.Read" 
$folders = Get-MgUserMailFolder -UserId $UPN -All 
write-host "Current folders:" 
$folders.DisplayName 
$folder = $folders | Where-Object { $_.DisplayName -eq "Inbox" } 

$mails = Get-MgUserMailFolderMessage -All -UserId $UPN -MailFolderId $folder.Id -Top 1 
Write-Host "No. Of Emails: $($mails.count)" 

foreach($currEmail in $mails){
    Write-Host "Subject: $($currEmail.Subject)" 

    # PidTagMessageSize = 0x0E08 
    # Can't get the right form for the following.... 
    
    $mailSizeInBytes = Get-MgUserMessageSingleValueExtendedProperty -InputObject $currEmail -Property "0x0E08" 
    # Errors as Get-MgUserMessageSingleValueExtendedProperty : The pipeline has been stopped. 
    
    $mailSizeInBytes = Get-MgUserMessageSingleValueExtendedProperty -MessageId $currEmail.Id -UserId $UPN -Property "0x0E08" 
    # Errors as Get-MgUserMessageSingleValueExtendedProperty : Parsing OData Select and Expand failed: An identifier was expected at position 0. 
    
    $mailSizeInBytes = Get-MgUserMessageSingleValueExtendedProperty -MessageId $currEmail.Id -UserId $UPN -Property "LONG 0x0E08" 
    # Errors as Get-MgUserMessageSingleValueExtendedProperty : Parsing OData Select and Expand failed: Term 'LONG 0x0E08' is not valid in a $select or $expand expression. 
    
    Write-Host "Mail Size: $($mailSizeInBytes)" 
}