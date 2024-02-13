# OpossumBot (now in v3!) and discord-picturebook (now in Alpha!)

OpossumBot v3 is a python module and bot core for posting funny Virginia Opossum (Didelphis virginiana) pictures to your [Discord App](https://discord.com) chats. Converted from `node.js` and brought to life using Python 3.11!

discord-picturebook is a python module to be used in conjunction with a properly configured `mysql` database, in order to modularize the capability of making your own discord picture bot, in the same way that the OpossumBot core does!  

# Info

`opossumbot` is a implementation of `discord-picturebook`, which is a implementation of `discord.py` and basic `mysql` queries, to post pictures of Opossums to discord chats!

# Runtime 

OpossumBot (will be) running aboard `hemisphere.contrastellar.com`, a personal server of [@contrastellar](https://github.com/contrastellar), and has no plans for future expansion as of January 2024.

## hemisphere.contrastellar.com

`hemisphere.contrastellar.com` is a [DigitalOcean](https://www.digitalocean.com/) droplet, with 4GB of Memory, 2 AMD vCPUs, and an 80 GB disk. It is currently privately managed by [@contrastellar](https://github.com/contrastellar) as a webhost for personal websites, and a remote Ubuntu compilation platform. The platform will likely be cleaned in the future.

# Installation 

## OpossumBot v3
```
TO BE IMPLEMENTED! PLEASE COME BACK LATER!
```

## discord-picturebook
```
TO BE IMPLEMENTED ON RELEASE! PLEASE COME BACK LATER!
```

# `discord-picturebook` usage

```py
import discord-picturebook
```

# Quickstart (/w conda)

## `conda` install

`conda` can be installed from [here](https://docs.conda.io/projects/conda/en/stable/user-guide/install/index.html).

## Once `conda` is installed

1. Clone the repo

2. Navigate to the cloned repo
```sh
cd ./OpossumBot_v3
```

3. Install the environment /w conda
```sh
conda env create --file environment.yml
```

4. Activate the environment
```sh
conda activate OpossumBot
```

5. `conda` handles all the installation of the packages and dependencies for these modules. A `requirements.txt` is maintained for both `virtualenv` users, and for GitHub Actions runtime simplicity.

# TODO
- [ ] Create sample Database and publish `.sql` files for user creation
  * update `README.md` with `discord-picturebook` installation and usage
- [ ] Create bot core for OpossumBot for alpha testing
- [ ] Edit existing workflow `.github/workflows/lint.yaml` to properly lint all `.py` files
- [ ] Create new workflows for testing, building, publishing, etc.
- [ ] ???
- [ ] Profit

# Contributing

Pull requests are welcome. For major changes, please open issues first to discuss what you would like to change.

# License

The license for `opossumbot` and `discord-picturebook` is the `GNU General Public License`. Please see [License](https://github.com/contrastellar/OpossumBot_v3/blob/main/LICENSE) for more information.

