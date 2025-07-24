# Types of Version Control Systems

A version control system is a tool that helps developers track and manage changes to a project's codebase over time. There are mainly two types:

- **Centralized Version Control Systems (CVCS)**
- **Distributed Version Control Systems (DVCS)**  
  *Git is a DVCS (GeeksforGeeks, n.d.).*

---

## Snapshots

A snapshot captures specific versions of application components and their associated deployment processes at a particular point in time. This facilitates consistent and repeatable deployments across various environments. Snapshots are typically created after successful deployments in testing environments and can be promoted through different stages of the delivery pipeline, ensuring that tested configurations are maintained throughout. This approach simplifies the management of complex deployments involving multiple teams and environments (IBM, n.d).

---

## What is a Repository? (Remote vs. Local)

A code repository, or "repo," is a centralized digital storage system where developers store, manage, and collaborate on an application's source code and related files. It facilitates version control, allowing teams to track changes, coordinate simultaneous edits, and maintain a comprehensive history of the project's evolution. This centralized approach enables efficient collaboration among developers, regardless of their physical locations, ensuring consistency and integrity throughout the software development lifecycle (Amazon Web Services, n.d.).

---

## What is a Commit?

A commit is an action similar to saving a file that has been edited. A commit documents a change to one or more files in your branch. During this process, Git assigns a unique ID, named SHA (Secure Hash Algorithm), that identifies what type of change, when, and who created it (GitHub, n.d.).

---

## What is the Working Directory?

A working directory is the folder on your computer where your commands are currently being executed. It's like your current location within the file system. When you create, open, or save files without specifying a full path, your computer uses this directory as the default location (Lenovo, n.d.).

---

## What is the Staging Area?

The development staging environment is a simulated version of the live environment that developers use to test for bugs and refine the code. After ensuring the code is error-free, it is moved to deployment, where it becomes accessible to users in the real application (McGregor, 2024).

---

## Diagram

Find a good diagram that illustrates the architecture and the flow:

*Source: [GeeksforGeeks - Git Flow vs. GitHub Flow](https://www.geeksforgeeks.org/git-flow-vs-github-flow/)*

---
## Advanced Exercises

If ChatGPT is a “blurry JPEG of the Web,” using such tools in academic, journalistic, or legal settings poses significant risks. Accuracy can suffer because the model may distort or omit important details, similar to how a compressed image loses clarity. Originality is also at risk, as AI-generated content often repackages existing information, which can raise concerns about plagiarism or lack of genuine insight. Additionally, accountability becomes problematic since AI lacks authorship and intent, making it difficult to assign responsibility for mistakes—an essential factor in fields that rely on factual precision and ethical standards. Overall, lossy AI-generated content can undermine trust and reliability unless carefully verified and transparently applied.

---
## References

- Amazon Web Services. (n.d.). What is AWS Code Commit? [https://aws.amazon.com/what-is/repo/](https://aws.amazon.com/what-is/repo/)
- GeeksforGeeks. (n.d.). Version Control Systems. [https://www.geeksforgeeks.org/version-control-systems/](https://www.geeksforgeeks.org/version-control-systems/)
- GitHub. (n.d.). Committing and reviewing changes to your project in GitHub Desktop. GitHub Docs. [https://docs.github.com/en/desktop/making-changes-in-a-branch/committing-and-reviewing-changes-to-your-project-in-github-desktop](https://docs.github.com/en/desktop/making-changes-in-a-branch/committing-and-reviewing-changes-to-your-project-in-github-desktop)
- IBM. (n.d.). Snapshots. IBM Documentation. [https://www.ibm.com/docs/en/devops-deploy/8.1.0?topic=deployment-snapshots](https://www.ibm.com/docs/en/devops-deploy/8.1.0?topic=deployment-snapshots)
- Lenovo. (n.d.). Understanding the working directory in computing. Lenovo US. [https://www.lenovo.com/us/en/glossary/working-directory/](https://www.lenovo.com/us/en/glossary/working-directory/)
- McGregor, M. (2024, August 5). Development staging explained. Built In. [https://builtin.com/articles/development-staging](https://builtin.com/articles/development-staging)
- Chiang, T. (2023 February 9). ChatGPT is a blurry JPEG of the Web. The Verge. [https://www.theverge.com/2023/2/9/23593064/chatgpt-openai-blurry-jpeg-web](https://github.com/granierregis/MSSE640-2025summer/blob/main/files/articles/BlurryJPG.pdf)