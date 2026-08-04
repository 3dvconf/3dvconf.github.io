---
layout: 2027_sidebar
year: 2027
title: Ethics Guidelines
---

*This document has been adapted from the [ECCV 2026 Ethics Guidelines](https://eccv.ecva.net/Conferences/2026/EthicsGuidelines), which are based on the [ECCV 2024 Ethics Guidelines](https://eccv.ecva.net/Conferences/2024/EthicsGuidelines), which were in turn adapted from the [CVPR 2024 Ethics Guidelines](https://cvpr.thecvf.com/Conferences/2024/EthicsGuidelines), the [CVPR 2022 Ethics Guidelines](https://cvpr2022.thecvf.com/ethics-guidelines) and the [NeurIPS 2021 Guidelines](https://nips.cc/public/EthicsGuidelines).*

As computer vision research and applications have increasing real-world impact, the likelihood of meaningful social benefit increases, but so does the attendant risk of harm. The research community should consider not only the potential benefits but also the potential negative societal impacts of computer vision research, and adopt measures that enable positive trajectories to unfold while mitigating risk of harm. This document should be used by authors, reviewers, and area chairs in order to develop a common understanding of important ethical principles for 3DV. During the 3DV review process, reviewers will have the ability to flag papers with significant ethical concerns. These will be referred to an ethics committee, which will assess the situation and advise the program chairs. The program chairs reserve the right to reject papers with grave ethical issues, but expect this to occur only in exceptional circumstances.

**Potential Negative Societal Impacts**: 3DV authors are invited to think about the potential negative societal impacts of their proposed research artifact or application. The ethics consequences of a paper can stem from either the methodology or the application. On the methodology side, for example, a new adversarial attack might give unbalanced power to malicious entities; in this case, defenses and other mitigation strategies would be expected, as is standard in computer security. On the application side, in some cases, the choice of application is incidental to the core contribution of the paper, and a potentially harmful application should be swapped out (as an extreme example, replacing ethnicity classification with bird classification), but the potential misuses should be still noted. In other cases, the core contribution might be inseparable from a questionable application (e.g., reconstructing a face given speech). In such cases, one should critically examine whether the scientific (and ethical) merits really outweigh the potential ethical harms.

A non-exhaustive list of potential negative societal impacts is included below. Consider whether the proposed methods and applications can:

1. Directly facilitate injury to living beings. For example: could it be integrated into weapons or weapons systems?

2. Raise safety, privacy, or security concerns. For example: is there a risk that applications could cause serious accidents or open security vulnerabilities when deployed in real-world environments? Would they make public people’s identity or other personal information without their consent?

3. Raise human rights concerns. For example: could the technology be used to discriminate, exclude, or otherwise negatively impact people, including impacts on the provision of vital services, such as healthcare and education, or limit access to opportunities like employment? Please consult the Toronto Declaration for further details.

4. Have a detrimental effect on people’s livelihood or economic security. For example: have a detrimental effect on people’s autonomy, dignity, or privacy at work? Could it be used to increase worker surveillance, or impose conditions that present a risk to the health and safety of employees?

5. Develop or extend harmful forms of surveillance. For example: could it be used to collect or analyze bulk surveillance data to predict immigration status or other protected categories, or be used in any kind of criminal profiling?

6. Severely damage the environment. For example: would the application incentivize significant environmental harms such as deforestation, hunting of endangered species, or pollution?

7. Deceive people in ways that cause harm. For example: could the approach be used to facilitate deceptive interactions that would cause harms such as theft, fraud, or harassment? Could it be used to impersonate public figures to influence political processes, or as a tool of hate speech or abuse?

Whenever a work is associated with significant potential negative impacts (or can be perceived that way by reviewers), submissions should include a discussion of these impacts. Such a discussion should consider different stakeholders that could be impacted, paying special attention to vulnerable or marginalized communities. It should also include possible mitigation strategies (e.g., gated release of models, providing defenses in addition to attacks, mechanisms for monitoring misuse, mechanisms to monitor how a system learns from feedback over time, improving the efficiency and accessibility of computer vision models, etc.).

Grappling with ethics is a difficult problem for our field, and thinking about ethics is still relatively new to many authors. A common difficulty with assessing ethical impact is its indirectness: most papers focus on general-purpose methodologies (e.g., object recognition algorithms), whereas ethical concerns are more apparent when considering deployed applications (e.g., surveillance systems). Also, real-world impact (both positive and negative) often emerges from the cumulative progress of many papers, so it is difficult to attribute the impact to an individual paper. In certain cases, the applications can have both significant risks and benefits, or it may not be possible to draw a bright line between ethical and unethical. Authors should not hesitate to acknowledge such ambiguities and err on the side of transparency.

**General Ethical Conduct**: We assume that all submissions adhere to ethical standards for responsible research practice and due diligence in the conduct. If the research uses human-derived data, consider – and discuss, where applicable – whether that data might:

1. Contain any personally identifiable information or sensitive personally identifiable information. For instance, does the dataset use features or label information about individual names? Did people provide their consent on the collection of such data? Could the use of the data be degrading or embarrassing for some people?

2. Contain information that could be deduced about individuals that they have not consented to share. For instance, a dataset with medical image annotations by experts could inadvertently disclose user information such as their name, depending on the features provided.

3. Encode, contain, or potentially exacerbate bias against people of a certain gender, race, sexuality, or who have other protected characteristics. For instance, does the dataset represent the diversity of the community where the approach is intended to be deployed?

4. Contain human subject experimentation and whether it has been reviewed and approved by a relevant oversight board. For instance, studies predicting characteristics (e.g., mental health status) from human data (e.g., performance of everyday activities) are expected to have their studies reviewed by an ethical board (IRB or equivalent).

5. Have been discredited by the creators. For instance, the DukeMTMC-ReID dataset has been taken down and it should not be used in 3DV submissions.

In general, there are other issues related to data that are worthy of consideration and review. These include:

1. Consent to use or share the data. Explain whether you have asked the data owner’s permission to use or share data and what the outcome was. Even if you did not receive consent, explain why this might be appropriate from an ethical standpoint. For instance, if the data was collected from a public forum, were its users asked consent to use the data they produced, and if not, why?

2. Domain specific considerations when working with high-risk groups. For example, if the research involves work with minors or vulnerable adults, have the relevant safeguards been put in place?

3. Filtering of offensive content. For instance, when collecting a dataset, how are the authors filtering offensive content such as pornographic or violent images?

4. Compliance with GDPR and other data-related regulations. For instance, if the authors collect human-derived data, what is the mechanism to guarantee individuals’ right to be forgotten (removed from the dataset)?

This list is not intended to be exhaustive — it is included here as a prompt for author and reviewer reflection.

Papers that violate these policies risk being removed from the conference and the proceedings.
