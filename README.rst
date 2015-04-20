============
Mail Mangler
============

A simple Django app providing template tags that attempt to obfuscate raw
e-mail addresses to make them ever so slightly more difficult to scrape.

To be as unobtrusive as possible, JavaScript is used to translate mangled
source into a normal e-mail address. If JS is not present, the reCAPTCHA
mailhide service is offered to deobfuscate the addresses.

Quick start
-----------

1. Add "mailhide" to your INSTALLED_APPS setting

2. Add MAILMANGLE_PUBLIC and MAILMANGLE_SECRET strings to the settings, with keys
   from the reCAPTCHA Mailhide API: http://www.google.com/recaptcha/mailhide/apikey

3. Add {% mailmangler_script %} to your template along with other JS

4. In templates with email addresses, pass the email variable to the mailmangle
   template tag.
