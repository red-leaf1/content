# query syntax is according to Carbon Black Enterprise Protection query language documented in https://developer.carbonblack.com/reference/enterprise-protection/7.2/rest-api/#query-condition - e.g. "name:*srv*"
res = []
dArgs = demisto.args()
if not "limit" in demisto.args():
    dArgs["limit"] = "10"
resCmd1 = demisto.executeCommand("cbp-computer-search", dArgs)
for entry in resCmd1:
    if isError(entry):
        res.append(entry)
    else:
        matches = entry["Contents"]
        if matches:
            res.append(  { "Type" : entryTypes["note"], "ContentsFormat" : formats["table"], "Contents" : matches } )
        else:
            res.append(  { "Type" : entryTypes["note"], "ContentsFormat" : formats["text"], "Contents" : "No matches." } )
demisto.results(res)