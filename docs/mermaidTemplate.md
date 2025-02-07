```mermaid

---
config:
    flowchart:
        defaultRenderer: elk
---

graph TD
Entity[#60;#60;rdfsClass#62;#62;<br /> <a class='internal-link is-unresolved' href='../../Entity'>Entity</a> ]
Event[#60;#60;rdfsClass#62;#62;<br /> <a class='internal-link is-unresolved' href='../../Event'>Event</a> ]
State[#60;#60;rdfsClass#62;#62;<br /> <a class='internal-link is-unresolved' href='../../State'>State</a> ]
PeriodOfTime[#60;#60;rdfsClass#62;#62;<br /> <a class='internal-link is-unresolved' href='../../PeriodOfTime'>PeriodOfTime</a> ]
EventParticipant[#60;#60;rdfsClass#62;#62;<br /> <a class='internal-link is-unresolved' href='../../EventParticipant'>EventParticipant</a> ]
isParticipationOf[#60;#60;objectProperty#62;#62;<br /> <a class='internal-link is-unresolved' href='../../isParticipationOf'>isParticipationOf</a> ]
isParticipantIn[#60;#60;objectProperty#62;#62;<br /> <a class='internal-link is-unresolved' href='../../isParticipantIn'>isParticipantIn</a> ]
relationship[#60;#60;objectProperty#62;#62;<br /> <a class='internal-link is-unresolved' href='../../relationship'>relationship</a> ]
ClassOfElement[#60;#60;rdfsClass#62;#62;<br /> <a class='internal-link is-unresolved' href='../../ClassOfElement'>ClassOfElement</a> ]


style ClassOfElement fill:#BAE8E8,stroke:#333,stroke-width:4px
style Thing fill:#F7F7F7,stroke:#333,stroke-width:4px
style Entity fill:#FFFF00,stroke:#333,stroke-width:4px
style State fill:#F5CC00,stroke:#333,stroke-width:4px
style Event fill:#ffb5c0,stroke:#333,stroke-width:4px
style PeriodOfTime fill:#fe9b38,stroke:#333,stroke-width:4px
style EventParticipant fill:#aF69EE,stroke:#333,stroke-width:4px
style isParticipationOf fill:#BFBFBF,stroke:#333,stroke-width:4px
style isParticipantIn fill:#BFBFBF,stroke:#333,stroke-width:4px
style relationship fill:#BFBFBF,stroke:#333,stroke-width:4px


--rdfsSubClassOf-->
--rdfsSubPropertyOf-->
--rdfsRange-->
--rdfsDomain-->


EntityInstance[#60;#60;ies:Entity#62;#62;<br /><u>EntityName</u>]
StateInstance[#60;#60;rdfsClass#62;#62;<br /><u>StateName</u>]
EventInstance[#60;#60;ies:Event#62;#62;<br /><u>EventName</u>]
PeriodOfTimeInstance[#60;#60;ies:ParticularPeriod#62;#62;<br /><u>TimeStamp</u>]
EventParticipantInstance[#60;#60; ies:EventParticipant#62;#62;<br /><u>Participant</u>]


style EntityInstance fill:black,stroke:#FFFF00,stroke-width:4px,color:#FFFF00
style State fill:black,stroke:#F5CC00,stroke-width:4px,color:#F5CC00
style EventInstance fill:black,stroke:#ffb5c0,stroke-width:4px,color:#ffb5c0
style PeriodOfTimeInstance fill:black,stroke:#fe9b38,stroke-width:4px,color:#fe9b38
style EventParticipantInstance fill:black,stroke:#aF69EE,stroke-width:4px,color:#aF69EE


--ies:isStartOf-->
--ies:inPeriod-->

```