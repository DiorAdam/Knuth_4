
def colorGraph(G):
    color = {}
    for w in G:
        if w in color:
            continue
        Link = [w]
        color[w] = 0
        while Link:
            u = Link.pop()
            for v in G[u]:
                if v not in color:
                    color[v] = 1-color[u]
                    Link.append(v)
                elif color[v] == color[u]:
                    return "not 2-colorable"
    return color

G = {}
G["a"], G["b"], G["c"] = {"b","c"}, {"a","e"}, {"a","d"}
G["d"], G["e"], G["f"], G["g"] = {"c"}, {"b","f","g"}, {"e","h"}, {"e","h"}
G["h"], G["i"], G["j"] = {"f","g"}, {"k","j"}, {"i","l", "m"}
G["k"], G["l"], G["m"] = {"i"}, {"j"}, {"j"}
c = colorGraph(G)
if type(c) != str:
    u, v = [s for s in c if c[s] == 0], [s for s in c if c[s] == 1]
    print(u)
    print(v)
else:
    print(c)


