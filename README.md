
# 🔗 Links
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/bilalelidrissi171/)


# sheets-downloader Program

## Introduction

This program is used to fetch data from a Google Sheet, Excel or CSV File and download it using Links

## Dependencies

Before you run this program, you need to install the following:

- Python
- pip

You also need to install the following libraries using pip:

- os-sys
- Google-auth
- Google-api-python-client
- requests
- pandas
## Format of Data
The format of the data in file should be like this:

| Name of File | Link of File |
| ------------ | ------------ |
| name1        | https://***  |
| name2        | https://***  |
| name3        | https://***  |


## Google Cloud Console Setup

If you want to get data from a Google Sheet, you need to set up the Google Cloud Console. Follow these steps:

- Go to https://console.cloud.google.com.
- Sign in with your Google account, or create a new account.
- Choose or create a project.
- Navigate to the "APIs & Services" dashboard and click on the "Library" tab.
- Search for the "Google Sheets API" and click on it.
- Click the "Enable" button to enable the API.
- Navigate to the "Credentials" tab and click on the "Create credentials" button.
- Select "Service account" as the type of credentials.
- Give the service account a name and select a role (e.g. "Editor").
- Click the "Create" button to generate a JSON key file.
- Download the JSON file and use its path in the os.environ["GOOGLE_APPLICATION_CREDENTIALS"] line of your code.
- Share the Google Sheet file with the public and get its link.

If you want to get data from a Excel or CSV file skip this setups

## Running the Program

To run the program, simply use the following command:

```bash
  git clone https://github.com/bilalelidrissi171/sheets-downloader.git
  cd sheets-downloader
  python sheets-downloader.py
```
## Contributing

Contributions to this project are welcome and appreciated! Here are two ways to contribute:

**Fork**

- Fork the project on GitHub

- Clone the project to your local machine git clone https://github.com/bilalelidrissi171/sheets-downloader.git

- Create a new branch git checkout -b new-feature

- Make your changes

- Commit your changes git commit -m 'Added new feature'

- Push to the remote branch git push origin new-feature

- Submit a pull request

**Issue**

- If you find a bug or have a feature request, please open a new issue
## License

[MIT](https://choosealicense.com/licenses/mit/)

