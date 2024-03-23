# ayane.dictionary

![release](https://img.shields.io/badge/release-v2.0--beta-DF1313)

___

A smart dictionary that can **memorize**, **edit**, and **find** words. The
main function of the dictionary is **efficient revision** of words. the dictionary will
remember which words the user knows worse than others, and then you will be
asked to repeat them. if the user knows the word perfectly, it will be displayed
less often than others.

<p align="center">
    <img src="https://raw.githubusercontent.com/kissmeandillkissumylove/ayane.
dictionary/master/.github/images/img0.png" width="80%">
</p>

___

# how to install

- you could download all the files from `code/code` and compile the executable
  **yourself**.
- or you could use the `.exe` I compiled from the `.github/download` directory.

___

# how to use

- there are two gray work screens.

    - the `top screen` is needed to display the word and transcription.
    - the `bottom screen` is used to display translations, hints and service
      messages.


- ![next](https://img.shields.io/badge/next-DF1313) button iterates through a
  `copy` of the list prepared for repeating words. not all words will be shown, but
  only those that the user is asked to repeat today.


- ![show](https://img.shields.io/badge/show-DF1313) button shows the translation
  of the word and everything that the user specified as a translation hint.


- ![right](https://img.shields.io/badge/right-32CD32) a button that the user clicks
  to confirm that they remembered the word or phrase correctly. this button
  increases the priority counter by `1`. when the counter reaches the number `3`,
  it will reset to `0`, and the word priority will increase by `1`. this way, the word
  will be shown to the user less frequently.

    - `example`: the user has `word@[wɜːd]@translation@2024-01-01@0@0` in a
      `database.txt`. the user decides to repeat this word on the **1 January** and
      answers correctly, and then saves everything. then the `database.txt` will
      have the following: `word@[wɜːd]@translation@2024-01-01@0@1`. then the
      user continues to revise this word for two days (or two times) and answers
      correctly. then in `database.txt` there will be the following:
      `word@[wɜːd]@translation@2024-01-04@1@0`. thus, the number after the
      date indicates the shift of this date by a certain number of days. therefore,
      now the word will be shown to the user **every other day**, and
      **not every day**.


- ![wrong](https://img.shields.io/badge/wrong-32CD32) button works like a
  ![right](https://img.shields.io/badge/right-32CD32) button, only the other way
  around. the counters of this button are negative and are responsible for showing
  the word to the user more often.


- ![again](https://img.shields.io/badge/again-DF1313) button prepares a new cycle
  of repeating words.


- ![save](https://img.shields.io/badge/save-2200AC) button saves all changes
  to a dictionary.


- ![add](https://img.shields.io/badge/add-19732E) button adds a new word to
  the dictionary. you can add a word without transcription, but not without the word
  itself or translation.


- ![find](https://img.shields.io/badge/find-19732E) button finds a word in the
  dictionary and displays it in text fields.


- ![edit](https://img.shields.io/badge/edit-19732E) button records the edited
  translation or transcription of the word, BUT **does not save it to a file**. be
  careful - always save your changes with the
  ![save](https://img.shields.io/badge/save-2200AC) button before exiting the app.


- `mistakes:` counts the number of mistakes.


- `words: A/B/C` `A` - the number of repeated words in the current loop. `B` -
  the number of words to revise today. `C` - how many words are there in
  `database.txt`.


- `word:`, `transcription:`, `translation:` are fields for filling in information about
  the word.


- `result:` field for displaying the result of executing different commands.
