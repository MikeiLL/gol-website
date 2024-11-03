---
id: 484
title: 'Real MadhaPPy Fans'
date: '2018-10-26T20:57:30+00:00'
layout: post
guid: 'https://giggleoutloud.com/?p=484'
permalink: /2018/10/26/real-madhappy-fans/
image: /wp-content/uploads/2018/10/Wagner.png
categories:
    - Projects
---

We’ve had the same mailing list for a long time. And like everything else, entropy degrades it. So it’s been time to update it.

We use a service called [SendInBlue](https://sendinblue.com) to send our emails.

They recommended to just create a new list with the people who have opened our emails. Only thing is, we just moved to them and have only sent about three emails. First thing we had done is use an email list cleaning service. We used [NeverBounce](https://neverbounce.com). Basically you upload a comma-separated file of all your emails and they return only the ones that are actually still valid emails. That cut our list down to about 50%. We did that before we even started using Send In Blue.

There were hundreds of fans and friends that hadn’t opened an email from us in a while. We haven’t had that much to say recently. So I downloaded all the addresses and names of people who hadn’t opened an email and added them as contacts on my MacBook.

Then hobbled together this script, mostly found on [StackOverflow](https://stackoverflow.com), which is so cool. It basically automatically does what I would have wanted to manually do for hundreds of emails.

It goes through all the contacts and one at a time, creates a message, waits a few seconds and sends it. The reason for the wait is so that the email provider doesn’t feel like it’s being attacked by a robot.

Dozens of people responded and we are adding those of you who want to be on it to the new “Real MadhaPPy Fans” email list.

Fun.

Enjoying some [Seth Faergolzia](https://www.patreon.com/SethFaergolzia).

```
set myMessage to "I'm cleaning up our mailing list. Please hit me back (or go to our site) if you want to be on the new one.

Thanks and I hope you are doing magically and wonderfully.

Blessings, Mike.
https://giggleoutloud.com
"

set mySubject to "New MadhaPPy email list"

display dialog "Please select the recipients in Address Book/Contacts"

tell application "Contacts"
    set theContacts to selection
    repeat with contact in theContacts
        set contact_name to name of contact
        if first name of contact is missing value then
            if name of contact is not missing value then
                set contact_addressed_as to name of contact
            else
                set contact_addressed_as to "stranger"
            end if
        else
            set contact_addressed_as to first name of contact
        end if
        my send_message(mySubject, "Hey " & contact_addressed_as & ",
" & return & myMessage, value of first email of contact)
        delay 10
    end repeat
end tell

on send_message(theSubject, theBody, theAddress)
    tell application "Mail"
        set theNewMessage to make new outgoing message with properties {sender:"Mike iLL <mike@madhappy.com>", subject:theSubject, content:theBody & return & return, visible:true}
        tell theNewMessage
            set visibile to true
            make new to recipient at end of to recipients with properties {address:theAddress}
            delay 3
            send
        end tell
    end tell
end send_message
display dialog "Sent batch ending with " & contact_name & "." buttons {"OK"}

```
