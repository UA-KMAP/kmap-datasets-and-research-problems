
# World Research Topics Network
The research topics network was created by analyzing millions of self-reported research topics on Google Scholar. The connections were extracted from co-occurrence of topics. 


![title](topics_network.png)

## Description of the network 
The research topics network is a node-edge-weighted undirected graph where each node is a research topic, and each edge represents the connection between two research topics. Node weight the importance of the topic #number of the researchers reported the topics in their profile. Edge weight represents the strength of the connection. 

# Load of the network
The dot file `topics_network_2019_release.dot` can be loaded as a networkx graph using the following code. 

```python
import networkx as nx 
import pygraphviz as pgv 
G=nx.Graph(pgv.AGraph('topics_network_2019_release.dot'))
```

The gpickle file can be loaded using the following code:
```python
import networkx as nx 
G=nx.read_gpickle("topics_network_2019_release.gpickle")
```

 

# Citation:
```bib
@inproceedings{Burd:2018:GGR:3206505.3206531,
 author = {Burd, Randy and Espy, Kimberly Andrews and Hossain, Md Iqbal and Kobourov, Stephen and Merchant, Nirav and Purchase, Helen},
 title = {GRAM: Global Research Activity Map},
 booktitle = {Proceedings of the 2018 International Conference on Advanced Visual Interfaces},
 series = {AVI '18},
 year = {2018},
 isbn = {978-1-4503-5616-9},
 location = {Castiglione della Pescaia, Grosseto, Italy},
 pages = {31:1--31:9},
 articleno = {31},
 numpages = {9},
 url = {http://doi.acm.org/10.1145/3206505.3206531},
 doi = {10.1145/3206505.3206531},
 acmid = {3206531},
 publisher = {ACM},
 address = {New York, NY, USA},
 keywords = {interactive visualization system, knowledge discovery, topics map},
}
```

[World Research Topics Networks: 
 Presentation](https://docs.google.com/presentation/d/1fnXOvxsteKfVldwEV3CWV2IZJ_-5eBBi3MMspGZKuzM/edit?usp=sharing)