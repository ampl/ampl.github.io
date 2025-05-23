balAssign0.dat
==============


.. warning::
    The original AMPL book does not reflect many of the latest features available in AMPL.
    For modern data transfer, we recommend using :ref:`APIs <apis>` such as our popular :ref:`Python API <python_integration>` or table handlers such as `amplxl <https://plugins.ampl.com/amplxl.html>`_.

    
    To explore examples showcasing these recent features, please visit:

    - `AMPL Streamlit Apps <https://ampl.com/streamlit/>`__
    - `AMPL+Python Book <https://ampl.com/mo-book/>`__
    - `AMPL Colab Notebooks <https://ampl.com/colab/>`__

:download:`balAssign0.dat <EXAMPLES/LOGIC/EXAMPLES/balAssign0.dat>`

.. code-block:: ampl

    
    # ------------------------------------------------
    # TEST DATA for balassign0.mod
    # All names and types are fictional
    # ------------------------------------------------
    
    param sample := 4;
    param selection := 0;
    
    param numberGrps := 7;
    
    set ALL_PEOPLE :=
       BIW   AJH   FWI   IGN   KWR   KKI   HMN   SML   RSR   TBR
       KRS   CAE   MPO   CAR   PSL   BCG   DJA   AJT   JPY   HWG
       TLR   MRL   JDS   JAE   TEN   MKA   NMA   PAS   DLD   SCG
       VAA   FTR   GCY   OGZ   SME   KKA   MMY   API   ASA   JLN
       JRT   SJO   WMS   RLN   WLB   SGA   MRE   SDN   HAN   JSG
       AMR   DHY   JMS   AGI   RHE   BLE   SMA   BAN   JAP   EHR
       MES   DHE   SWS   ACI   RJY   TWD   MMA   JJR   MFR   LHS
       JAD   CWU   PMY   CAH   SJH   EGR   JMQ   GGH   MMH   JWR
       MJR   EAZ   WAD   LVN   DHR   ABE   LSR   MBT   AJU   SAS
       JRS   RFS   TAR   DLT   HJO   SCR   CMY   GDE   MSL   CGS
       HCN   JWS   RPR   RCR   RLS   DSF   MNA   MSR   PSY   MET
       DAN   RVY   PWS   CTS   KLN   RDN   ANV   LMN   FSM   KWN
       CWT   PMO   EJD   AJS   SBK   JWB   SNN   PST   PSZ   AWN
       DCN   RGR   CPR   NHI   HKA   VMA   DMN   KRA   CSN   HRR
       SWR   LLR   AVI   RHA   KWY   MLE   FJL   ESO   TJY   WHF
       TBG   FEE   MTH   RMN   WFS   CEH   SOL   ASO   MDI   RGE
       LVO   ADS   CGH   RHD   MBM   MRH   RGF   PSA   TTI   HMG
       ECA   CFS   MKN   SBM   RCG   JMA   EGL   UJT   ETN   GWZ
       MAI   DBN   HFE   PSO   APT   JMT   RJE   MRZ   MRK   XYF
       JCO   PSN   SCS   RDL   TMN   CGY   GMR   SER   RMS   JEN
       DWO   REN   DGR   DET   FJT   RJZ   MBY   RSN   REZ   BLW ;
    
    param: CATEG: typeWt :=  dept 1  loc 1  rate 1  title 1 ;
    
    param type:
    
         dept       loc     rate    title   :=
    BIW   NNE   Peoria        A   Assistant
    KRS   WSW   Springfield   B   Assistant
    TLR   NNW   Peoria        B   Adjunct
    VAA   NNW   Peoria        A   Deputy
    JRT   NNE   Springfield   A   Deputy
    AMR   SSE   Peoria        A   Deputy
    MES   NNE   Peoria        A   Consultant
    JAD   NNE   Peoria        A   Adjunct
    MJR   NNE   Springfield   A   Assistant
    JRS   NNE   Springfield   A   Assistant
    HCN   SSE   Peoria        A   Deputy
    DAN   NNE   Springfield   A   Adjunct
    CWT   NNE   Springfield   A   Adjunct
    DCN   NNE   Peoria        A   Adjunct
    SWR   WSW   Peoria        A   Adjunct
    TBG   NNE   Springfield   A   Assistant
    LVO   NNE   Peoria        A   Assistant
    ECA   NNE   Springfield   A   Assistant
    MAI   NNE   Peoria        B   Adjunct
    JCO   SSE   Macomb        A   Adjunct
    DWO   SSE   Peoria        A   Adjunct
    AJH   NNE   Peoria        A   Adjunct
    CAE   SSE   Peoria        A   Adjunct
    MRL   WSW   Peoria        A   Assistant
    FTR   NNE   Peoria        A   Adjunct
    SJO   NNE   Peoria        A   Adjunct
    DHY   NNE   Urbana        A   Adjunct
    DHE   NNE   Peoria        A   Adjunct
    CWU   NNW   Peoria        A   Assistant
    EAZ   NNE   Peoria        A   Assistant
    RFS   NNE   Peoria        A   Deputy
    JWS   WSW   Peoria        A   Adjunct
    RVY   NNE   Peoria        A   Adjunct
    PMO   SSE   Peoria        A   Assistant
    RGR   NNE   Peoria        A   Assistant
    LLR   NNE   Peoria        A   Assistant
    FEE   NNW   Springfield   A   Adjunct
    ADS   NNE   Peoria        A   Adjunct
    CFS   NNW   Joliet        A   Assistant
    DBN   SSE   Peoria        A   Adjunct
    PSN   NNE   Peoria        A   Adjunct
    REN   NNE   Peoria        B   Adjunct
    FWI   NNW   Peoria        A   Assistant
    MPO   SSE   Peoria        A   Assistant
    JDS   NNW   Peoria        A   Adjunct
    GCY   NNE   Peoria        A   Adjunct
    WMS   NNE   Springfield   A   Deputy
    JMS   NNE   Springfield   A   Adjunct
    SWS   NNW   Springfield   A   Assistant
    PMY   NNE   Peoria        A   Deputy
    WAD   NNE   Springfield   A   Adjunct
    TAR   NNE   Peoria        A   Assistant
    RPR   NNE   Peoria        A   Adjunct
    PWS   NNE   Peoria        A   Consultant
    EJD   WSW   Peoria        B   Adjunct
    CPR   NNE   Peoria        A   Deputy
    AVI   NNE   Springfield   B   Adjunct
    MTH   NNE   Joliet        A   Assistant
    CGH   NNE   Springfield   A   Adjunct
    MKN   WSW   Peoria        A   Assistant
    HFE   NNW   Carbondale    A   Adjunct
    SCS   NNE   Peoria        A   Adjunct
    DGR   NNE   Springfield   A   Assistant
    IGN   NNE   Springfield   A   Assistant
    CAR   NNW   Peoria        A   Assistant
    JAE   NNE   Springfield   A   Assistant
    OGZ   NNE   Peoria        A   Consultant
    RLN   SSE   Peoria        A   Adjunct
    AGI   SSE   Peoria        A   Assistant
    ACI   NNE   Peoria        B   Assistant
    CAH   SSE   Peoria        B   Adjunct
    LVN   NNE   Springfield   B   Assistant
    DLT   SSE   Peoria        B   Adjunct
    RCR   NNE   Peoria        A   Adjunct
    CTS   NNE   Peoria        A   Deputy
    AJS   SSE   Peoria        A   Assistant
    NHI   NNE   Carbondale    A   Assistant
    RHA   NNW   Carbondale    A   Assistant
    RMN   NNE   Springfield   A   Deputy
    RHD   SSE   Peoria        A   Assistant
    SBM   NNW   Peoria        A   Assistant
    PSO   NNE   Peoria        A   Adjunct
    RDL   NNW   Joliet        A   Adjunct
    DET   NNE   Springfield   A   Assistant
    KWR   NNE   Peoria        A   Assistant
    PSL   SSE   Peoria        B   Assistant
    TEN   NNW   Springfield   A   Adjunct
    SME   NNE   Springfield   A   Consultant
    WLB   NNE   Peoria        A   Adjunct
    RHE   NNE   Peoria        A   Assistant
    RJY   SSE   Springfield   A   Deputy
    SJH   NNE   Cairo         A   Adjunct
    DHR   SSE   Peoria        A   Assistant
    HJO   NNE   Carbondale    A   Assistant
    RLS   NNE   Peoria        A   Adjunct
    KLN   WSW   Peoria        A   Adjunct
    SBK   NNE   Cairo         A   Adjunct
    HKA   NNE   Carbondale    A   Adjunct
    KWY   NNE   Peoria        A   Deputy
    WFS   NNW   Peoria        A   Adjunct
    MBM   SSE   Peoria        A   Assistant
    RCG   SSE   Peoria        A   Adjunct
    APT   NNE   Peoria        A   Adjunct
    TMN   NNE   Peoria        A   Assistant
    FJT   WSW   Peoria        A   Assistant
    KKI   NNE   Carbondale    A   Adjunct
    BCG   NNE   Urbana        A   Adjunct
    MKA   NNE   Carbondale    A   Assistant
    KKA   NNE   Peoria        A   Assistant
    SGA   NNW   Springfield   B   Assistant
    BLE   NNE   Peoria        A   Assistant
    TWD   SSE   Peoria        A   Assistant
    EGR   NNE   Peoria        B   Adjunct
    ABE   NNW   Peoria        A   Adjunct
    SCR   NNE   Peoria        A   Adjunct
    DSF   NNW   Springfield   A   Adjunct
    RDN   NNE   Peoria        A   Adjunct
    JWB   NNW   Peoria        B   Deputy
    VMA   SSE   Peoria        A   Adjunct
    MLE   NNE   Macomb        A   Adjunct
    CEH   NNE   Springfield   A   Assistant
    MRH   NNE   Peoria        A   Deputy
    JMA   NNE   Carbondale    A   Deputy
    JMT   NNE   Peoria        B   Assistant
    CGY   NNE   Springfield   A   Adjunct
    RJZ   NNW   Peoria        A   Adjunct
    HMN   WSW   Springfield   B   Assistant
    DJA   NNE   Peoria        A   Adjunct
    NMA   NNE   Carbondale    B   Assistant
    MMY   NNE   Peoria        A   Assistant
    MRE   NNE   Peoria        A   Assistant
    SMA   NNE   Joliet        A   Adjunct
    MMA   NNE   Carbondale    A   Deputy
    JMQ   NNE   Carbondale    B   Assistant
    LSR   NNW   Peoria        A   Adjunct
    CMY   NNE   Peoria        A   Adjunct
    MNA   NNE   Carbondale    A   Adjunct
    ANV   SSE   Peoria        A   Assistant
    SNN   NNE   Macomb        B   Deputy
    DMN   NNW   Peoria        A   Adjunct
    FJL   NNE   Springfield   A   Assistant
    SOL   NNE   Evansville    A   Assistant
    RGF   NNE   Springfield   A   Adjunct
    EGL   NNE   Peoria        A   Adjunct
    RJE   NNE   Macomb        A   Adjunct
    GMR   NNE   Peoria        A   Assistant
    MBY   NNE   Peoria        B   Assistant
    SML   NNE   Springfield   A   Assistant
    AJT   NNE   Peoria        A   Assistant
    PAS   NNE   Peoria        A   Assistant
    API   NNE   Springfield   A   Adjunct
    SDN   NNE   Peoria        A   Deputy
    BAN   NNE   Peoria        A   Assistant
    JJR   SSE   Springfield   A   Adjunct
    GGH   NNW   Peoria        A   Adjunct
    MBT   NNE   Peoria        A   Adjunct
    GDE   NNE   Peoria        A   Deputy
    MSR   SSE   Peoria        A   Assistant
    LMN   NNW   Peoria        B   Assistant
    PST   NNE   Springfield   A   Assistant
    KRA   NNE   Peoria        A   Adjunct
    ESO   NNE   Springfield   A   Adjunct
    ASO   NNE   Carbondale    B   Assistant
    PSA   NNE   Springfield   A   Assistant
    UJT   NNE   Springfield   A   Assistant
    MRZ   WSW   Peoria        B   Assistant
    SER   NNW   Peoria        A   Assistant
    RSN   NNE   Joliet        A   Assistant
    RSR   NNW   Peoria        A   Adjunct
    JPY   NNE   Peoria        A   Adjunct
    DLD   NNE   Urbana        B   Assistant
    ASA   SSE   Peoria        A   Consultant
    HAN   SSE   Peoria        A   Deputy
    JAP   SSE   Peoria        A   Adjunct
    MFR   NNE   Springfield   A   Adjunct
    MMH   NNE   Joliet        A   Adjunct
    AJU   SSE   Springfield   A   Assistant
    MSL   NNW   Springfield   A   Adjunct
    PSY   NNE   Springfield   A   Assistant
    FSM   NNE   Springfield   A   Assistant
    PSZ   SSE   Peoria        A   Assistant
    CSN   NNE   Joliet        A   Assistant
    TJY   WSW   Springfield   A   Adjunct
    MDI   NNE   Peoria        A   Consultant
    TTI   NNE   Carbondale    A   Assistant
    ETN   NNE   Peoria        A   Assistant
    MRK   NNE   Peoria        A   Adjunct
    RMS   NNE   Peoria        A   Adjunct
    REZ   NNE   Evansville    A   Adjunct
    TBR   NNE   Peoria        A   Deputy
    HWG   NNE   Peoria        A   Assistant
    SCG   NNW   Joliet        A   Adjunct
    JLN   NNE   Peoria        B   Assistant
    JSG   NNE   Peoria        A   Deputy
    EHR   NNE   Peoria        A   Assistant
    LHS   NNE   Peoria        A   Adjunct
    JWR   NNE   Springfield   A   Assistant
    SAS   NNE   Peoria        B   Adjunct
    CGS   NNE   Springfield   A   Assistant
    MET   NNE   Peoria        B   Assistant
    KWN   WSW   Springfield   A   Assistant
    AWN   NNE   Springfield   A   Adjunct
    HRR   NNE   Macomb        A   Adjunct
    WHF   NNE   Peoria        A   Assistant
    RGE   SSE   Springfield   A   Adjunct
    HMG   NNE   Joliet        B   Assistant
    GWZ   NNE   Joliet        A   Assistant
    XYF   NNE   Peoria        A   Assistant
    JEN   NNE   Peoria        A   Deputy
    BLW   NNE   Peoria        A   Deputy ;
    
