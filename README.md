<div align="center">
  <h1>Hacktoberfest</h1>
	<p><b><i>Let's Contribute To Open-source</i></b></p>
</div>

# First Contributions

This project aims to simplify and guide the way, beginners can make their first contribution towards open-source. If you are looking to make your first contribution, follow the steps below.

## Fork this repository

Fork this repository by clicking on the fork button on the top of this page.
This will create a copy of this repository in your account.

## Clone the repository

Now clone the forked repository to your machine. Go to your GitHub account, open the forked repository, click on the code button and then click the _copy to clipboard_ icon.

Open a terminal and run the following git command:

```
git clone "url you just copied"
```

where "url you just copied" (without the quotation marks) is the url to this repository (your fork of this project). See the previous steps to obtain the url.

For example:

```
git clone https://github.com/your-username/Hacktoberfest.git
```

where `your-username` is your GitHub username. Here you're copying the contents of the first-contributions repository on GitHub to your computer.

## Create a branch

Change to the repository directory on your computer (if you are not already there):

```
cd Hacktoberfest
```

Now create a branch using the `git switch` command:

```
git switch -c your-new-branch-name
```

For example:

```
git switch -c add-ehmad-saeed
```

## Make your changes and commit those changes

Now open `Contributors.md` file in a text editor, add your name to it. Now, save the file.

If you go to the project directory and execute the command `git status`, you'll see there are some changes.

Add those changes to the branch you just created using the `git add` command:

```
git add Contributors.md
```

Now commit those changes using the `git commit` command:

```
git commit -m "Add your-name to the Contributors list"
```

replacing `your-name` with your username.

## Push changes to GitHub

Push your changes using the command `git push`:

```
git push origin -u your-branch-name
```

replacing `your-branch-name` with the name of the branch you created earlier.

# Create a PR for review

If you go to current repository on GitHub, you'll see a `Compare & pull request` button. Click on that button. Now submit the pull request.

Soon I'll be merging all your changes into the main branch of this project and adding `hactoberfest-accepted` tag to your PR. You will get a notification email once the changes have been merged.

## What's next?

Congrats! You just completed the standard _fork -> clone -> edit -> pull request_ workflow that you'll often encounter as a contributor!
Now you can search for `beginner-friendly` and `good first issue` tags on GitHub and contribute to those projects.

Happy coding! 🎉

## 🔑 License & Conduct

- MIT © [Ehmad Saeed](https://github.com/justEhmadSaeed)
- [Code of Conduct](https://github.com/justEhmadSaeed/Hacktoberfest/blob/main/CODE_OF_CONDUCT.md)
