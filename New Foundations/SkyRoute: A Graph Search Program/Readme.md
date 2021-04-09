# SkyRoute: A Graph Search Program
Vancouver’s public metro system has asked us to help create a program to help commuters get from one landmark to another. We’ll be building out “SkyRoute,” a routing tool that uses breadth-first search, depth-first search, and Python dictionaries to accomplish this feat. For the purposes of this project, we will assume that it takes the same amount of time to get from each station to each of its connected neighboring stations.

  - graph_search.py has the bfs() and dfs() functions implemented in Python
  - vc_metro.py contains a graph of all stations in the Vancouver metro system
  - vc_landmarks.py contains a dictionary of Vancouver landmarks mapped to their nearest metro station(s)
  - landmark_choices.py contains a dictionary of letters of the alphabet mapped to landmarks to make it easier for users to make a selection
