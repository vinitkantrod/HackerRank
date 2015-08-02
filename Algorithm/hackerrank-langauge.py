import re
l = []
li = "C:CPP:JAVA:PYTHON:PERL:PHP:RUBY:CSHARP:HASKELL:CLOJURE:BASH:SCALA: ERLANG:CLISP:LUA:BRAINFUCK:JAVASCRIPT:GO:D:OCAML:R:PASCAL:SBCL:DART: GROOVY:OBJECTIVEC"
li = li.split(':')
for i in range(input()):
    a = raw_input()
    a1 = a.split()
    m = re.match('^[\d]+\s[\w]*$',a)
    if m:
        if a1[1] in li:
            l.append("VALID")
        else:
            l.append("INVALID")
for e in l:
    print e
    
