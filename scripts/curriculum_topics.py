"""Registry for the extended MAIS PAC HTML-first curriculum (07–10)."""
TOPICS = [
 {'code':'07.01','key':'windows','title':'Multi-wavelength Astronomy','group':6,'group_name':'Instrumentation and Space Technologies'},
 {'code':'07.02','key':'telescope','title':'Instrumentation','group':6,'group_name':'Instrumentation and Space Technologies'},
 {'code':'08.01','key':'root','title':'Numerical Methods','group':7,'group_name':'Mathematical Methods and Tools'},
 {'code':'08.02','key':'calculus','title':'Basic Calculus','group':7,'group_name':'Mathematical Methods and Tools'},
 {'code':'08.03','key':'vectors','title':'Vectors','group':7,'group_name':'Mathematical Methods and Tools'},
 {'code':'08.04','key':'geometry','title':'Geometric Instruments','group':7,'group_name':'Mathematical Methods and Tools'},
 {'code':'08.05','key':'stats','title':'Statistics & Error Analysis','group':7,'group_name':'Mathematical Methods and Tools'},
 {'code':'09.01','key':'nakedeye','title':'Naked-Eye Observations','group':8,'group_name':'Practical Part'},
 {'code':'09.02','key':'skymap','title':'Sky Maps and Catalogues','group':8,'group_name':'Practical Part'},
 {'code':'09.03','key':'coords','title':'Observational Coordinates and Estimates','group':8,'group_name':'Practical Part'},
 {'code':'09.04','key':'exposure','title':'Astronomical Instruments','group':8,'group_name':'Practical Part'},
 {'code':'10.01','key':'errors','title':'Error Sources','group':8,'group_name':'Practical Part'},
 {'code':'10.02','key':'fit','title':'Graphs and Best Fit','group':8,'group_name':'Practical Part'},
 {'code':'10.03','key':'doublestar','title':'Geometrical Instruments in Practice','group':8,'group_name':'Practical Part'},
 {'code':'10.04','key':'photometry','title':'Experimental Techniques','group':8,'group_name':'Practical Part'},
]
BY_CODE={t['code']:t for t in TOPICS}
PROBLEMS_PER_TOPIC=10
