# IPhO study guides

The IPhO section on the Teaching page links three introductory HTML-first guides: theoretical skills, experimental skills and data analysis, and mathematics. The material is original MAIS PAC practice, not official IPhO questions or Savchenko problems. It is not a complete, topic-by-topic IPhO curriculum; the syllabus is the coverage checklist. Use the official past papers to practise integrated, timed theoretical and experimental problems.

The attached 2014/2015 syllabus is preserved as `teaching/pdf/ipho-syllabus-supplied.pdf`. `ipho-syllabus.pdf` is a reading copy with a provenance cover, not a newly issued official syllabus. The [IPhO syllabus webpage](https://www.ipho-new.org/statutes-syllabus/) was consulted on 1 November 2026; it does not clearly identify a more recent revision date. Its equipment list explicitly mentions transistors, unlike the supplied PDF. Consult the webpage and contest organisers for current requirements.

Build and check:

```sh
python scripts/build_ipho.py
python scripts/build_ipho_syllabus.py  # requires PyMuPDF and reportlab
python scripts/test_ipho.py           # requires Beautiful Soup and PyMuPDF
```

Use a working environment with the dependencies in `requirements.txt`. The existing handout audit checks structural problems; it is not a proof of scientific correctness. Substantial further authoring and independent review are needed before these guides can be considered comprehensive or error-free.
