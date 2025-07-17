from models.Project import Project
from models.Course import Course
from models.DocumentObject import DocumentObject
from firebase.config import db
from firebase.operations import get_all_projects, get_project_metadata
from firebase.file_operations import upload_pptx_to_firebase, get_download_link
from utils.json_utils import id_json
import pprint
d = """{
  "title": "Engineering Education Research Course Document",
  "description": "A comprehensive document outlining the structure, content, policies, and resources for a course on research design in engineering education.",
  "children": [
    {
      "title": "Module 0: Course Overview and Foundations",
      "description": "This module provides an introduction to the course, including its objectives, structure, assessment methods, and essential university policies and resources.",
      "children": [
        {
          "title": "Lesson 0.1: Course Introduction and Objectives",
          "description": "Understand the fundamental purpose and learning outcomes of the course, along with administrative details.",
          "children": [
            {
              "title": "Topic 0.1.1: Course Information",
              "description": "General details about the course, including its code, section, class times, location, and academic term.",
              "rawContent": "EGN 6020 Section 28696\nClass Periods: T 5-6, R 6\nLocation: NSC 520\nAcademic Term: Fall 2024"
            },
            {
              "title": "Topic 0.1.2: Instructor Information",
              "description": "Details about the course instructor, including contact information and office hours.",
              "rawContent": "Jeremy A. Magruder Waisome\nNuclear Science Building 202C\njwaisome@eng.ufl.edu\nOffice Phone: 352-294-3637\nOffice Hours: R 5"
            },
            {
              "title": "Topic 0.1.3: Course Description and Pre-requisites",
              "description": "An overview of the course content, focusing on research design in engineering education, and any prerequisites.",
              "rawContent": "Fundamentals of research design in engineering education research. How to select a research approach that aligns with a research question, principles of research design, management of data, and ethics of human subject research.\nCourse Pre-Requisites / Co-Requisites: None"
            },
            {
              "title": "Topic 0.1.4: Course Objectives",
              "description": "Specific learning outcomes students are expected to achieve by the end of the course.",
              "rawContent": "Focuses on the fundamentals of research design in engineering education. Particular attention will be paid to the relationship between how a study is designed and the valid assessment of study results and conclusions. There will be an emphasis on understanding the linkages between theory, empirical statements or research questions, study objectives, study design, and valid inferences or conclusions. The principles of various research designs including true experiments, quasi-experiments, and qualitative studies will be discussed with particular emphasis on how each is better or worse at dealing with various issues of both internal and external validity.\nThe specific objectives for this course are:\n*   Understanding the major concepts involved in designing and conducting research\n*   Understanding how to construct different types of research designs and the strengths and limitations of each approach\n*   Developing strong capabilities in the following areas: (1) Writing a proposal, (2) Conducting a literature review, and (3) Managing data\n*   Reviewing how engineering education research is conducted and how it informs our understanding of learning and teaching practices\n*   Applying the designs and concepts learned in class to a real-world research design\n*   Understanding the differences between causality and correlation and be able to construct a narrative about relationships"
            },
            {
              "title": "Topic 0.1.5: Required Materials and Textbooks",
              "description": "Information on required readings and software for the course.",
              "rawContent": "Materials and Supply Fees: None\nRequired Textbooks and Software:\n*   Title: Research Design: Qualitative, Quantitative, and Mixed Methods Approaches\n*   Author: John W. Creswell, J. David Creswell\n*   Publication date and edition: Nov. 8, 2022, 6th Edition\n*   ISBN Number: 978-1071817940\nAdditional Readings: Find new references that are relevant"
            }
          ]
        },
        {
          "title": "Lesson 0.2: Course Policies and Expectations",
          "description": "Guidelines for student conduct, attendance, academic integrity, and support services.",
          "children": [
            {
              "title": "Topic 0.2.1: Attendance and Make-Up Policy",
              "description": "Expectations for class attendance and procedures for excused absences.",
              "rawContent": "This course is interactive so attendance in expected. Excused absences must be in compliance with university policies in the Graduate Catalog (http://gradcatalog.ufl.edu/content.php?catoid=10&navoid=2020#attendance) and require appropriate documentation."
            },
            {
              "title": "Topic 0.2.2: Grading Policy and Evaluation",
              "description": "Breakdown of assignments, their weight in the final grade, and the grading scale.",
              "rawContent": "Evaluation of Grades:\nAssignment | Total Points | Percentage of Final Grade\nOnline Postings (8) | 100 each | 20%\nHomework Assignments (2) (Literature Review and Comparisons of Research Design) | 100 each | 20%\nPeer Reviews (3) | 100 each | 6%\nRequired trainings (IRB) | 100 each | 4%\nFinal Project (Part 1): Research Design Proposal | 100 | 30%\nFinal Project (Part 2): Presentation | 100 | 20%\nTotal: 100%\n\nGrading Policy:\nPercent | Grade | Grade Points\n93.4 - 100 | A | 4.00\n90.0 - 93.3 | A- | 3.67\n86.7 - 89.9 | B+ | 3.33\n83.4 - 86.6 | B | 3.00\n80.0 - 83.3 | B- | 2.67\n76.7 - 79.9 | C+ | 2.33\n73.4 - 76.6 | C | 2.00\n70.0 - 73.3 | C- | 1.67\n66.7 - 69.9 | D+ | 1.33\n63.4 - 66.6 | D | 1.00\n60.0 - 63.3 | D- | 0.67\n0 - 59.9 | E | 0.00\nMore information on UF grading policy may be found at: https://catalog.ufl.edu/ugrad/current/regulations/info/grades.aspx"
            },
            {
              "title": "Topic 0.2.3: Assignment Details",
              "description": "Detailed descriptions of the types of assignments, including online postings, homework, peer reviews, and the final project.",
              "rawContent": "Online posting on course reading/listening/viewing assignments (20%):\nWe will use the course readings from the required textbooks and additional readings/listening/viewing content as the central basis for our discussion. The purpose of this assignment is for you to reflect on the content and summarize it in a concise manner prior to discussion in class. In addition, this is an opportunity for you to shape some of the course discussions on these topics. Questions you may answer (you do not have to address them all in every post):\n*   What were the clearest takeaways from the content?\n*   What were the most confusing parts of the content?\n*   What did you learn that could have practical usefulness?\n*   What new concepts or theories did you encounter?\n*   What was the most unexpected thing you learned from the week’s content?\n*   How did the in-class discussion and/or presentation (where applicable) enhance your understanding of the week's topic? Did the class impact your initial understanding of the topic in any way?\n*   How, if at all, have this week’s course readings or discussions influenced your research interests?\n\nHomework Assignments (20%):\nLength: 4-page max, double-spaced\nEveryone is expected to work on the following two different homework assignments:\n1) Literature Review: Submit a preliminary literature review related to your research interest based on at least 5 papers or journal articles of your choice. Students can decide on the type of review they want to conduct, like the systematic literature review, qualitative review, etc.\n2) Comparisons on Research Designs: Select three research designs of your choice and do a comparative analysis based on when their use is most appropriate. Extend this analysis to include design choices that are appropriate for carrying out various types of studies around your research interest.\n\nPeer Review (6%):\nStudents will review one other student’s HW and final research design proposal and provide them with written feedback. The feedback will be structured by shouldtemplate provided by the instructor. This assignment helps students develop skills in self-regulation in learning to judge the quality of their own writing by comparing it to peers, and develop their capacity as critical, constructive, and compassionate peer reviewers of others' work. Both these skills are critical to doing successful graduate-level research.\n\nOnline Training (4%):\nEveryone is expected to complete the required IRB and CITI training and submit their completion certificates on e-learning.\n\nFinal Project: Research Design Proposal + Presentation (50%):\nEveryone is expected to work on a research design proposal around an engineering education-based research question of their choice. You are expected to:\n*   Select appropriate research methods,\n*   Design a study with a step-by-step description of how the data will be collected,\n*   Formulate a data management plan, and\n*   Write an ethics statement that deals with addressing the ethical issues in conducting the study.\nAs a part of the research design proposal, students are expected to also situate the research questions in the relevant literature. Students will submit the proposal document and give a presentation in which they are expected to justify the study design in the context of the research questions and answer questions pertaining to the validity and interpretability of the study. Students can apply for IRB approval of the study design, but it is not required."
            },
            {
              "title": "Topic 0.2.4: Academic Integrity and Conduct",
              "description": "University policies on honesty, software use, and student privacy.",
              "rawContent": "University Honesty Policy:\nUF students are bound by The Honor Pledge which states, “We, the members of the University of Florida community, pledge to hold ourselves and our peers to the highest standards of honor and integrity by abiding by the Honor Code. On all work submitted for credit by students at the University of Florida, the following pledge is either required or implied: “On my honor, I have neither given nor received unauthorized aid in doing this assignment.” The Honor Code (https://sccr.dso.ufl.edu/policies/student-honor-code-student-conduct-code/) specifies a number of behaviors that are in violation of this code and the possible sanctions. Furthermore, you are obligated to report any condition that facilitates academic misconduct to appropriate personnel. If you have any questions or concerns, please consult with the instructor or TAs in this class.\n\nSoftware Use:\nAll faculty, staff, and students of the University are required and expected to obey the laws and legal agreements governing software use. Failure to do so can lead to monetary damages and/or criminal penalties for the individual violator. Because such violations are also against University policies and rules, disciplinary action will be taken as appropriate. We, the members of the University of Florida community, pledge to uphold ourselves and our peers to the highest standards of honesty and integrity.\n\nStudent Privacy:\nThere are federal laws protecting your privacy with regards to grades earned in courses and on individual assignments. For more information, please see: https://registrar.ufl.edu/ferpa.html"
            },
            {
              "title": "Topic 0.2.5: Support and Resources",
              "description": "Information on academic accommodations, course evaluations, and various campus health and academic resources.",
              "rawContent": "Students Requiring Accommodations:\nStudents with disabilities who experience learning barriers and would like to request academic accommodations should connect with the Disability Resource Center by visiting https://disability.ufl.edu/students/get-started/. It is important for students to share their accommodation letter with their instructor and discuss their access needs, as early as possible in the semester.\n\nCourse Evaluation:\nStudents are expected to provide professional and respectful feedback on the quality of instruction in this course by completing course evaluations online via GatorEvals. Guidance on how to give feedback in a professional and respectful manner is available at https://gaterevals.aa.ufl.edu/students/. Students will be notified when the evaluation period opens, and can complete evaluations through the email they receive from GatorEvals, in their Canvas course menu under GatorEvals, or via https://ufl.bluera.com/ufl/. Summaries of course evaluation results are available to students at https://gaterevals.aa.ufl.edu/public-results/.\n\nCommitment to a Safe and Inclusive Learning Environment:\nThe Herbert Wertheim College of Engineering values broad diversity within our community and is committed to individual and group empowerment, inclusion, and the elimination of discrimination. It is expected that every person in this class will treat one another with dignity and respect regardless of gender, sexuality, disability, age, socioeconomic status, ethnicity, race, and culture.\nIf you feel like your performance in class is being impacted by discrimination or harassment of any kind, please contact your instructor or any of the following:\n*   Your academic advisor or Graduate Program Coordinator\n*   Robin Bielling, Director of Human Resources, 352-392-0903, rbielling@eng.ufl.edu\n*   Curtis Taylor, Associate Dean of Student Affairs, 352-392-2177, taylor@eng.ufl.edu\n*   Toshikazu Nishida, Associate Dean of Academic Affairs, 352-392-0943, nishida@eng.ufl.edu\n\nCampus Resources:\nHealth and Wellness:\nU Matter, We Care: Your well-being is important to the University of Florida. The U Matter, We Care initiative is committed to creating a culture of care on our campus by encouraging members of our community to look out for one another and to reach out for help if a member of our community is in need. If you or a friend is in distress, please contact umatter@ufl.edu so that the U Matter, We Care Team can reach out to the student in distress. A nighttime and weekend crisis counselor is available by phone at 352-392-1575. The U Matter, We Care Team can help connect students to the many other helping resources available including, but not limited to, Victim Advocates, Housing staff, and the Counseling and Wellness Center. Please remember that asking for help is a sign of strength. In case of emergency, call 9-1-1.\nCounseling and Wellness Center: http://www.counseling.ufl.edu/cwc, and 392-1575; and the University Police Department: 392-1111 or 9-1-1 for emergencies.\n\nSexual Discrimination, Harassment, Assault, or Violence:\nIf you or a friend has been subjected to sexual discrimination, sexual harassment, sexual assault, or violence contact the Office of Title IX Compliance, located at Yon Hall Room 427, 1908 Stadium Road, (352) 273-1094, title-ix@ufl.edu\nSexual Assault Recovery Services (SARS): Student Health Care Center, 392-1161.\nUniversity Police Department at 392-1111 (or 9-1-1 for emergencies), or http://www.police.ufl.edu/.\n\nAcademic Resources:\nE-learning technical support, 352-392-4357 (select option 2) or e-mail to Learning-support@ufl.edu. https://lss.at.ufl.edu/help.shtml.\nCareer Resource Center, Reitz Union, 392-1601. Career assistance and counseling. https://www.crc.ufl.edu/.\nLibrary Support, http://cms.uflib.ufl.edu/ask. Various ways to receive assistance with respect to using the libraries or finding resources.\nTeaching Center, Broward Hall, 392-2010 or 392-6420. General study skills and tutoring. https://teachingcenter.ufl.edu/.\nWriting Studio, 302 Tigert Hall, 846-1138. Help brainstorming, formatting, and writing papers. https://writing.ufl.edu/writing-studio/.\nStudent Complaints Campus: https://care.dso.ufl.edu.\nOn-Line Students Complaints: http://www.distance.ufl.edu/student-complaint-process."
            }
          ]
        }
      ]
    },
    {
      "title": "Module 1: Foundations of Engineering Education Research",
      "description": "This module introduces students to the core philosophical underpinnings and theoretical frameworks of research in engineering education.",
      "children": [
        {
          "title": "Lesson 1.1: Introduction to Research and Philosophical Foundations",
          "description": "Explore the fundamental nature of research and its philosophical basis within engineering education.",
          "children": [
            {
              "title": "Topic 1.1.1: What is Research?",
              "description": "Discussion on the definition of research, focusing on its philosophical foundations in engineering education.",
              "rawContent": "What is Research? Exploring the philosophical foundations of engineering education research.\nAssignment: Online posting 1: Introductory discussion"
            }
          ]
        },
        {
          "title": "Lesson 1.2: Theory, Design Categories, and Epistemology",
          "description": "Delve into the role of theory, different categories of research design, and epistemological perspectives in engineering education.",
          "children": [
            {
              "title": "Topic 1.2.1: Theory and Category of Design",
              "description": "Understanding the interplay between theoretical frameworks and the classification of research designs, including perspectives on epistemology in engineering education.",
              "rawContent": "Theory and category of design and perspectives on epistemology in engineering education.\nAssignment: Online posting 2: Positionality"
            }
          ]
        }
      ]
    },
    {
      "title": "Module 2: Literature Review and Research Question Formulation",
      "description": "This module focuses on developing essential skills for conducting structured literature reviews and formulating precise engineering education research questions.",
      "children": [
        {
          "title": "Lesson 2.1: Structured Literature Review and Research Questions",
          "description": "Learn methodologies for conducting structured literature reviews and techniques for identifying relevant research questions in engineering education.",
          "children": [
            {
              "title": "Topic 2.1.1: Structured Literature Review and Identifying Research Questions",
              "description": "Techniques for conducting systematic literature reviews and methods for developing strong research questions specific to engineering education.",
              "rawContent": "Structured literature review and identifying engineering education research questions.\nAssignment: Online posting 3: Research questions"
            }
          ]
        }
      ]
    },
    {
      "title": "Module 3: Data, Variables, Sampling, and Research Approaches",
      "description": "This module covers the different types of data, variable measurement, sampling techniques, and an overview of various research approaches in engineering education.",
      "children": [
        {
          "title": "Lesson 3.1: Data, Variables, Sampling, and Research Approaches",
          "description": "Explore how to categorize and measure data, select appropriate sampling methods, and understand various research approaches in engineering education.",
          "children": [
            {
              "title": "Topic 3.1.1: Types of Engineering Education Data",
              "description": "Understanding different data types, methods for measuring and defining variables, appropriate sampling strategies, and an overview of research approaches relevant to engineering education.",
              "rawContent": "Types of engineering education data, measuring and defining variables, sampling, research approaches in engineering education.\nAssignment: HW1: Literature Review, Online posting 4: Purpose statement"
            }
          ]
        },
        {
          "title": "Lesson 3.2: Experimental and Quasi-Experimental Design",
          "description": "Focus on the principles and applications of experimental and quasi-experimental research designs.",
          "children": [
            {
              "title": "Topic 3.2.1: Experimental and Quasi-Experimental Design",
              "description": "Detailed discussion on the characteristics, strengths, and limitations of experimental and quasi-experimental designs in research.",
              "rawContent": "Experimental design, quasi-experimental design.\nAssignment: Peer review on HW1"
            }
          ]
        }
      ]
    },
    {
      "title": "Module 4: Survey Design and Validation",
      "description": "This module is dedicated to the principles of designing and validating surveys for research purposes.",
      "children": [
        {
          "title": "Lesson 4.1: Survey Design and Validation",
          "description": "Learn the methodologies behind constructing effective surveys and the processes for validating their reliability and validity.",
          "children": [
            {
              "title": "Topic 4.1.1: Survey Design and Validation",
              "description": "Principles of designing robust surveys and the techniques required to validate them for research use.",
              "rawContent": "Survey design and validation.\nAssignment: Online posting 5: Hypothesis statement"
            }
          ]
        }
      ]
    },
    {
      "title": "Module 5: Mixed Methods and Case Studies",
      "description": "This module introduces mixed methods research designs and the application of case study approaches.",
      "children": [
        {
          "title": "Lesson 5.1: Mixed Methods and Case Studies",
          "description": "Explore the integration of quantitative and qualitative methods in mixed methods designs and the in-depth approach of case studies.",
          "children": [
            {
              "title": "Topic 5.1.1: Mixed Methods Study Design and Introduction to Case Studies",
              "description": "Understanding how to combine different research methods and the foundational aspects of conducting case studies.",
              "rawContent": "Mixed methods study design and introduction to case studies.\nAssignment: Online posting 6: Non-traditional research methods, HW2 Draft: Comparisons on Research Designs"
            }
          ]
        }
      ]
    },
    {
      "title": "Module 6: Ethics in Human Subjects Research",
      "description": "This module covers the critical aspects of ethical considerations, Institutional Review Board (IRB) processes, and human subjects' research.",
      "children": [
        {
          "title": "Lesson 6.1: IRB, Human Subjects Research, and Ethics",
          "description": "Understand the guidelines and procedures for conducting ethical research involving human participants, including IRB protocols.",
          "children": [
            {
              "title": "Topic 6.1.1: IRB, Human Subjects' Research, and Ethics in Research",
              "description": "Comprehensive overview of ethical principles in research, the role of the Institutional Review Board (IRB), and best practices for human subjects' research.",
              "rawContent": "IRB, human subjects' research, and ethics in research.\nAssignment: Required IRB training completion"
            }
          ]
        }
      ]
    },
    {
      "title": "Module 7: Designing Research Proposals",
      "description": "This module focuses on the practical skills required for designing and writing comprehensive research proposals in engineering education.",
      "children": [
        {
          "title": "Lesson 7.1: Designing Research Proposals",
          "description": "Learn the components and structure of effective research proposals in engineering education.",
          "children": [
            {
              "title": "Topic 7.1.1: Designing Research Proposals in Engineering Education",
              "description": "Practical guidance on structuring and writing compelling research proposals tailored for engineering education studies.",
              "rawContent": "Designing research proposals in engineering education.\nAssignment: Peer review on HW2 draft"
            }
          ]
        },
        {
          "title": "Lesson 7.2: Proposal Finalization",
          "description": "Finalize and submit the second homework assignment, applying the learned research design comparison skills.",
          "children": [
            {
              "title": "Topic 7.2.1: Research Design Comparisons Submission",
              "description": "Submission of the comprehensive comparison of research designs.",
              "rawContent": "No specific topic content; this week is dedicated to the submission of Homework Assignment 2.\nAssignment: HW2: Comparisons on Research Designs"
            }
          ]
        }
      ]
    },
    {
      "title": "Module 8: Research Design Proposal Discussion and Data Considerations",
      "description": "This module provides a platform for discussing research design proposals and delves into advanced considerations for data, including validity, interpretability, and causality.",
      "children": [
        {
          "title": "Lesson 8.1: Research Design Proposal Discussion",
          "description": "Engage in discussions and receive feedback on individual research design proposals.",
          "children": [
            {
              "title": "Topic 8.1.1: Research Design Proposal Discussion",
              "description": "Interactive session for reviewing and discussing proposed research designs.",
              "rawContent": "Research design proposal discussion.\nAssignment: Online posting 7"
            }
          ]
        },
        {
          "title": "Lesson 8.2: Data Management and Considerations",
          "description": "Focus on effective strategies for data management in research.",
          "children": [
            {
              "title": "Topic 8.2.1: Data Management",
              "description": "Best practices and strategies for organizing, storing, and maintaining research data.",
              "rawContent": "Data management.\nAssignment: Online posting 8"
            }
          ]
        },
        {
          "title": "Lesson 8.3: Advanced Data Considerations",
          "description": "Explore crucial aspects of data quality, interpretation, and the nuances of causal relationships.",
          "children": [
            {
              "title": "Topic 8.3.1: Data Considerations: Validity, Interpretability, Directionality, Causality, and Comparison Groups",
              "description": "In-depth analysis of factors influencing data validity, interpretability, understanding directionality, establishing causality, and the role of comparison groups in research.",
              "rawContent": "Data considerations: validity, interpretability, directionality, causality, and comparison groups.\nAssignment: Research design proposals (Final Project Part 1 Submission)"
            }
          ]
        },
        {
          "title": "Lesson 8.4: Causation and Correlation",
          "description": "A dedicated discussion on differentiating between causation and correlation in research findings.",
          "children": [
            {
              "title": "Topic 8.4.1: Discussion on Regression Analysis (Causation and Correlation)",
              "description": "Understanding the distinction between correlation and causation, particularly in the context of regression analysis.",
              "rawContent": "Discussion on regression analysis (causation and correlation)."
            }
          ]
        }
      ]
    },
    {
      "title": "Module 9: Final Project Presentation",
      "description": "This module culminates in the presentation of the final research design proposals and peer feedback.",
      "children": [
        {
          "title": "Lesson 9.1: Final Presentation and Peer Review",
          "description": "Students will present their final research design proposals and participate in peer reviews.",
          "children": [
            {
              "title": "Topic 9.1.1: Final Presentation",
              "description": "Students present their comprehensive research design proposals to the class.",
              "rawContent": "Final presentation.\nAssignment: Peer reviews on research design proposals"
            }
          ]
        }
      ]
    }
  ]
}"""

prj_id = '54de001b-e07e-4a2c-9931-85d2a958bce1'
path = 'H:\\notebooks\Graduation project\\finaaal\ITI-Graduation-Project\\temp\presentation.pptx'

outpath = upload_pptx_to_firebase(path,prj_id)
print('='*50)
print(outpath)

#pprint.pprint(id_json("this_id_25656",d))
