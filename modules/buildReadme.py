from main import *


def buildReadmeDotMd():
    vars.finalReadme = f"""
<div align="center">
[<a href='{vars.rproject_url}/releases'>Releases</a>]&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;[<a href='{vars.rproject_url}/issues'>Issues</a>]&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;[<a href='{vars.rproject_url}#readme'>Homepage</a>]&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;[<a href='{vars.rproject_url}/pulls'>Pull Request</a>]&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;[<a href='{vars.rproject_url}/wiki'>Wiki</a>]&nbsp;&nbsp;&nbsp;

</div>
<div align="center">
<a href="{vars.rproject_url}" title="">
<img src="https://img.shields.io/badge/version-{vars.prVersion}-blue.svg?style=for-the-badge&logo=appveyor" alt="Version - {vars.prVersion}">
</a>
<a href="{vars.rproject_url}" title="">
<img src="https://img.shields.io/badge/documentation-yes-brightgreen.svg?style=for-the-badge" alt="Maintenance">
</a>
<a href="{vars.rproject_url}/LICENSE.md" target="_blank">
<img alt="License: ISC" src="https://img.shields.io/github/license/{func.getLicenseBadgeThing(vars.rproject_url)}?style=for-the-badge" />
</a>
</div>
        """
    if vars.prDescription != '':
        vars.finalReadme = vars.finalReadme + f"""

## 📘 Description
<div align="center">
{vars.prDescription}
</div>
        """

    if vars.prHomePage != '':
        vars.finalReadme = vars.finalReadme + f"""
## 🏠 [Homepage]({vars.prHomePage})

Visit this project repository [here]({vars.prHomePage}) and let us know your opinion :D
        """
    if vars.prDoscsUrl != '':
        vars.finalReadme = vars.finalReadme + f"""
## 🌠 [Documents]({vars.prDoscsUrl})

Check out our documentation for more information!
* Click Here -> [📚 Docs]({vars.prDoscsUrl}) 
        """

    if vars.prIssuesUrl != '':
        vars.finalReadme = vars.finalReadme + f"""\n
## 🌟 Issues/Contribute

* Report your issues here: [Report Here]({vars.finalIssues})
* Contribute with your amazing ideas: [Contribute Here]({vars.finalPulls})
"""

    if vars.prAuthorName != '':
        vars.finalReadme = vars.finalReadme + f"""
## 👤 Author

 **{vars.prGithubUsername}**

* Github: [@{vars.prGithubUsername}](https://github.com/{vars.prGithubUsername})
"""
    if vars.prWebSite != '':
        vars.finalReadme = vars.finalReadme + f"* Website: {vars.prWebSite}"

    if vars.prLicenseName != '':
        vars.finalReadme = vars.finalReadme + f"""\n
## 📝 License

Copyright © {now.year} [{vars.prGithubUsername}](https://github.com/{vars.prGithubUsername}).<br />
This project is [{vars.prLicenseName}]({vars.rproject_url}/blob/master/LICENSE) licensed.
"""
    vars.finalReadme = vars.finalReadme + f"""
## 
_Star this project ⭐️ if it helped you!_

***
<div align="right">
<a href='https://github.com/IMXNOOBX/readme-generator'>💎</a>
</div>


<!-- Made with: https://github.com/IMXNOOBX/readme-generator - ISC - 2022 - IMXNOOBX -->
    """
    if func.checkFileExists('readme.md'):
        os.remove("readme.md")
    file = open("README.md", "w", encoding='utf-8')
    file.write(vars.finalReadme)
    file.close()
