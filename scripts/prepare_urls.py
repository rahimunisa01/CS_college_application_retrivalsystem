import json

university_urls = [
    {"name": "MIT", "url": "https://www.eecs.mit.edu/graduate-programs/graduate-admissions/"},
    {"name": "Stanford University", "url": "https://cs.stanford.edu/admissions/masters"},
    {"name": "Carnegie Mellon University", "url": "https://www.ml.cmu.edu/prospective-students/apply.html"},
    {"name": "UC Berkeley", "url": "https://eecs.berkeley.edu/academics/graduate/masters"},
    {"name": "Princeton University", "url": "https://gradschool.princeton.edu/academics/fields-study/computer-science"},
    {"name": "Harvard University", "url": "https://gsas.harvard.edu/admissions/apply"},
    {"name": "Caltech", "url": "https://www.cms.caltech.edu/academics/grad/cs"},
    {"name": "Cornell University", "url": "https://www.cs.cornell.edu/ms/apply"},
    {"name": "UCLA", "url": "https://www.cs.ucla.edu/graduate-admission/"},
    {"name": "University of Washington", "url": "https://www.cs.washington.edu/academics/grad/mcs"},
    {"name": "University of Illinois Urbana-Champaign", "url": "https://cs.illinois.edu/admissions/graduate/apply"},
    {"name": "Georgia Institute of Technology", "url": "https://www.cc.gatech.edu/future/graduate/mscs"},
    {"name": "Yale University", "url": "https://cpsc.yale.edu/graduate/graduate-admissions"},
    {"name": "Johns Hopkins University", "url": "https://www.cs.jhu.edu/graduate-studies/graduate-admissions/"},
    {"name": "Columbia University", "url": "https://www.cs.columbia.edu/education/ms/admissions/"},
    {"name": "New York University (NYU)", "url": "https://cs.nyu.edu/home/graduate/admissions.html"},
    {"name": "University of Texas at Austin", "url": "https://www.cs.utexas.edu/graduate-program/masters-program"},
    {"name": "UC San Diego", "url": "https://cse.ucsd.edu/graduate/graduate-admissions"},
    {"name": "University of Pennsylvania", "url": "https://www.cis.upenn.edu/graduate/masters-admissions/"},
    {"name": "University of Chicago", "url": "https://masters.cs.uchicago.edu/page/admissions"},
    {"name": "University of Southern California", "url": "https://viterbigradadmission.usc.edu/programs/masters/ms-programs/computer-science/"},
    {"name": "University of Michigan–Ann Arbor", "url": "https://cse.engin.umich.edu/academics/graduate/admissions/"},
    {"name": "UC Santa Barbara", "url": "https://cs.ucsb.edu/graduate/graduate-admissions"},
    {"name": "UC Davis", "url": "https://cs.ucdavis.edu/graduate/apply"},
    {"name": "University of Wisconsin–Madison", "url": "https://www.cs.wisc.edu/graduate/admissions/"},
    {"name": "UNC Chapel Hill", "url": "https://cs.unc.edu/graduate/admissions/"},
    {"name": "Northwestern University", "url": "https://www.mccormick.northwestern.edu/computer-science/graduate/admissions.html"},
    {"name": "Duke University", "url": "https://gradschool.duke.edu/academics/programs/computer-science/"},
    {"name": "Brown University", "url": "https://cs.brown.edu/grad/masters/apply/"},
    {"name": "University of Florida", "url": "https://www.cise.ufl.edu/graduate/masters/"}
]

with open("data/university_urls.json", "w") as f:
    json.dump(university_urls, f, indent=4)

print("✅ URL list saved.")
