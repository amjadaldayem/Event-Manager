## event-manager
=====================
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/9f29bf9dc6dc4bb498b7ff21aca4a267)](https://www.codacy.com/app/mashhoodr/event-manager?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=recurship/event-manager&amp;utm_campaign=Badge_Grade)
[![Commitizen friendly](https://img.shields.io/badge/commitizen-friendly-brightgreen.svg)](http://commitizen.github.io/cz-cli/)

This is a simple event manager app - built to learn Django REST and React.

### Setup

To run the backend simply have Docker installed on your machine and run `make up`

If you are running the first time you will need to run `make migrate && make loaddata` to run the migrations and load sample data

To run the frontend you can use:
- cd client
- npm install
- npm start

We will later move this into its own docker image.


### Scope

The scope of the application is very simple. We are looking to create a simple event management application, where our
local community leaders can manage their events, and notify anybody subscribed to an event or organisation with updates.
We will maintain tickets as issues

### Commit Message Format

We will need to do `npm run commit` and then will get the prompts needed to start a commit!

[![Add and commit with Commitizen](https://github.com/commitizen/cz-cli/raw/master/meta/screenshots/add-commit.png)](https://github.com/commitizen/cz-cli/raw/master/meta/screenshots/add-commit.png)

### Editor Settings for VSCode

```bash
update the VSCode settings with following

{
"editor.formatOnSave": true,
 "[javascript]": {
   "editor.formatOnSave": false,
   "editor.tabSize": 2,
   "editor.insertSpaces": false,
   "editor.detectIndentation": false
 },
 "prettier.disableLanguages": [
   "js"
 ],
 "eslint.autoFixOnSave": true,
 "eslint.alwaysShowStatus": true,
 "editor.tabSize": 2,
 "editor.insertSpaces": true,
 "editor.detectIndentation": false,
 "css.validate": true
}
```

