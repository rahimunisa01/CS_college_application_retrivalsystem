import json

university_urls = [
    {"name": "MIT", "url": "https://www.eecs.mit.edu/academics/graduate-programs/admission-process/"},
    {"name": "Stanford University", "url": "https://www.cs.stanford.edu/admissions-graduate-application-deadlines"},
    {"name": "Carnegie Mellon University", "url": "https://admissions.scs.cmu.edu/portal/apply_gr"},
    {"name": "UC Berkeley", "url": "https://grad.berkeley.edu/program/computer-science/"},
    {"name": "Princeton University", "url": "https://gradschool.princeton.edu/academics/fields-study/computer-science"},
    {"name": "Harvard University", "url": "https://gsas.harvard.edu/admissions/apply"},
    {"name": "Caltech", "url": "https://www.cms.caltech.edu/academics/grad/grad_cs"},
    {"name": "Cornell University", "url": "https://www.cs.cornell.edu/masters/apply/application"},
    {"name": "UCLA", "url": "https://www.cs.ucla.edu/graduate-admission/"},
    {"name": "University of Washington", "url": "https://www.uwb.edu/stem/graduate/mscsse/admissions"},
    {"name": "University of Illinois Urbana-Champaign", "url": "https://siebelschool.illinois.edu/admissions/graduate/applications-process-requirements"},
    {"name": "Georgia Institute of Technology", "url": "https://www.cc.gatech.edu/ms-computer-science-admission-requirements"},
    {"name": "Yale University", "url": "https://gsas.yale.edu/programs-of-study/computer-science"},
    {"name": "Johns Hopkins University", "url": "https://www.cs.jhu.edu/academic-programs/graduate-studies/"},
    {"name": "Columbia University", "url": "https://www.cs.columbia.edu/education/ms/admissions/"},
    {"name": "New York University (NYU)", "url": "https://engineering.nyu.edu/admissions/graduate/apply/application-deadlines"},
    {"name": "University of Texas at Austin", "url": "https://www.cs.utexas.edu/graduate-program/masters-program"},
    {"name": "UC San Diego", "url": "https://cse.ucsd.edu/graduate/cse-graduate-application-checklist"},
    {"name": "University of Pennsylvania", "url": "https://www.cis.upenn.edu/graduate/program-offerings/master-of-computer-and-information-technology/"},
    {"name": "University of Chicago", "url": "https://masters.cs.uchicago.edu/admissions/dates-deadlines/"},
    {"name": "University of Southern California", "url": "https://viterbigradadmission.usc.edu/programs/masters/ms-programs/computer-science/"},
    {"name": "University of Michigan–Ann Arbor", "url": "https://cse.engin.umich.edu/academics/graduate/admissions/"},
    {"name": "UC Santa Barbara", "url": "https://cs.ucsb.edu/education/graduate/how-to-apply"},
    {"name": "UC Davis", "url": "https://grad.ucdavis.edu/program-application-deadlines"},
    {"name": "University of Wisconsin–Madison", "url": "https://www.cs.wisc.edu/graduate/admissions/"},
    {"name": "UNC Chapel Hill", "url": "https://cs.unc.edu/graduate/admissions/"},
    {"name": "Northwestern University", "url": "https://www.mccormick.northwestern.edu/computer-science/graduate/admissions.html"},
    {"name": "Duke University", "url": "https://gradschool.duke.edu/academics/programs-degrees/computer-science-ms/"},
    {"name": "Brown University", "url": "https://graduateprograms.brown.edu/graduate-program/computer-science-scm"},
    {"name": "University of Florida", "url": "https://www.cise.ufl.edu/graduate/masters/"}
]

with open("data/university_urls.json", "w") as f:
    json.dump(university_urls, f, indent=4)

print("✅ URL list saved.")
