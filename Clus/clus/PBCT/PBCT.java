/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package clus.PBCT;

import clus.PBCT.approaches.PBCTApproach;
import clus.data.io.ARFFFile;
import clus.data.io.ClusReader;
import clus.data.io.ClusView;
import clus.data.rows.RowData;
import clus.data.type.ClusSchema;
import clus.main.Settings;
import clus.util.ClusException;
import java.io.IOException;
import jeans.util.IntervalCollection;

/**
 *
 * @author zamith
 */
public class PBCT {
    PBCTApproach m_PBCTApproach;
    RowData m_VerticalData;
    ClusSchema m_VerticalSchema;
    
    RowData m_HorizontalData;
    ClusSchema m_HorizontalSchema;
    
    Settings m_Sett;
    
    public PBCT(Settings sett, PBCTApproach approach) throws IOException, ClusException{
        this.m_PBCTApproach = approach;
        this.m_Sett = sett;
        this.m_HorizontalData = m_PBCTApproach.getDataHorizontal();
        this.m_HorizontalSchema = m_HorizontalData.getSchema();
        
        ARFFFile arff = null;
        ClusReader reader = new ClusReader("outputVerticalData.arff", m_Sett);
        arff = new ARFFFile(reader);
	m_VerticalSchema = arff.read(m_Sett);
        initializeSettings(m_Sett);
        
        ClusView view = m_VerticalSchema.createNormalView();
	m_VerticalData = view.readData(reader, m_VerticalSchema);
	reader.close();
    }
    
    public void initializeSettings(Settings sett) throws ClusException, IOException {
		m_VerticalSchema.setSettings(sett);
		m_VerticalSchema.setTestSet(-1); /* Support ID for XVAL attribute later on? */
		m_VerticalSchema.setTarget(new IntervalCollection(getVerticalTargetInterval()));
		//m_VerticalSchema.setDisabled(new IntervalCollection(sett.getDisabled()));
		m_VerticalSchema.setClustering(new IntervalCollection(getVerticalTargetInterval()));
		m_VerticalSchema.setDescriptive(new IntervalCollection(getVerticalDescriptiveInterval()));
		//m_VerticalSchema.setKey(new IntervalCollection(sett.getKey()));
		m_VerticalSchema.updateAttributeUse();
		m_VerticalSchema.addIndices(ClusSchema.ROWS);
    }
    
    public String getVerticalTargetInterval(){
        int beginTarget = m_VerticalSchema.getNbAttributes() - m_HorizontalData.getNbRows() + 1;
        int endTarget = m_VerticalSchema.getNbAttributes();
        return(beginTarget+"-"+endTarget);
    }
    
    public String getVerticalDescriptiveInterval(){
        int beginTarget = m_VerticalSchema.getNbAttributes() - m_HorizontalData.getNbRows() + 1;
        return(1+"-"+(beginTarget-1));
    }
}
