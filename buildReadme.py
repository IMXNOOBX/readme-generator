from main import *

def buildReadmeDotMd():
    global finalReadme
    finalReadme = f"""
<div align="center">
[Releases]({rproject_url}/releases)&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;[Issues]({rproject_url}/issues)&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;[Homepage]({rproject_url}#readme)&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;[Pull Request]({rproject_url}/pulls)&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;[Wiki]({rproject_url}/wiki)&nbsp;&nbsp;&nbsp;

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
    finalReadme = finalReadme + f"""## 
***
_Star this project ⭐️ if it helped you!_<p align="right">[💎](https://github.com/IMXNOOBX/readme-generator)</p>
    """
    if checkFileExist.checkFileExists('readme.md'):
        os.remove("readme.md")
    file = open("README.md", "w", encoding='utf-8') 
    file.write(finalReadme) 
    file.close() 