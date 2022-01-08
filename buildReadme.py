from main import *

def buildReadmeDotMd(prDescription, prHomePage, prDoscsUrl, prAuthorName, prGithubUsername, prWebSite, prLicenseName, rproject_url):
    global finalReadme
    finalReadme = f"""
<div align="center">
[<a href='{rproject_url}/releases'>Releases</a>]&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;[<a href='{rproject_url}/issues'>Issues</a>]&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;[<a href='{rproject_url}#readme'>Homepage</a>]&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;[<a href='{rproject_url}/pulls'>Pull Request</a>]&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;[<a href='{rproject_url}/wiki'>Wiki</a>]&nbsp;&nbsp;&nbsp;

</div>
<div align="center">
    <a href="{rproject_url}" title="">
        <img src="https://img.shields.io/badge/version-{prVersion}-blue.svg?style=for-the-badge&logo=appveyor" alt="Version - {prVersion}">
    </a>
    <a href="{rproject_url}" title="">
        <img src="https://img.shields.io/badge/documentation-yes-brightgreen.svg?style=for-the-badge" alt="Maintenance">
    </a>
    <a href="{rproject_url}/LICENSE.md" target="_blank">
        <img alt="License: ISC" src="https://img.shields.io/github/license/{getLicenseBadgeThing(rproject_url)}?style=for-the-badge" />
    </a>
</div>
    """
    if prDescription != '':
        finalReadme = finalReadme + f"""
## 📘 Description
<div align="center">
{prDescription}
</div>
        """

    if prHomePage != '':
        finalReadme = finalReadme + f"""
### 🏠 [Homepage]({prHomePage})
        """
    if prDoscsUrl != '':
        finalReadme = finalReadme + f"""
## 🌠 [Documents]({prDoscsUrl})
        """
    if prAuthorName != '':
        finalReadme = finalReadme + f"""
## Author

👤 **{prGithubUsername}**

* Github: [@{prGithubUsername}](https://github.com/{prGithubUsername})
"""
    if prWebSite != '':
        finalReadme = finalReadme + f"* Website: {prWebSite}"

    if prLicenseName != '':
        finalReadme = finalReadme + f"""\n
## 📝 License

Copyright © {now.year} [{prGithubUsername}](https://github.com/{prGithubUsername}).<br />
This project is [{prLicenseName}]({rproject_url}/blob/master/LICENSE) licensed.
"""
    finalReadme = finalReadme + f"""
## 

***
<div style="display: flex; justify-content: space-between;">
_Star this project ⭐️ if it helped you!_ 
<p align="right">[💎](https://github.com/IMXNOOBX/readme-generator)</p>
</div>


<!-- Made with: https://github.com/IMXNOOBX/readme-generator - ISC - 2022 - IMXNOOBX -->
    """
    if checkFileExist.checkFileExists('readme.md'):
        os.remove("readme.md")
    file = open("README.md", "w", encoding='utf-8') 
    file.write(finalReadme) 
    file.close() 