# Three Lane Road Env
Simple three lane motorway environment implementing a new Gym env, following guidance [here](https://github.com/openai/gym/blob/master/docs/creating-environments.md).

This environment *will* reproduce observations and actions involved in driving along a congested motorway.

To use environment, install the package with `pip install -e three-lane-env`, and then create an instance of the environment with `gym.make('three_lane_env:three-lane-env-v0')`.
