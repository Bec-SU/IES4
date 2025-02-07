import pylode

html = pylode.MakeDocco(
    input_data_file="./IES Specification Docs/ies4.ttl",
    outputformat="html",
    profile="ontdoc"
).document("./docs/ies4.html")
