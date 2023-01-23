import sys
sys.path.append('../StatsUFC/model')

from BaseParse import ParserYuristOnline
from TestHelper import gt_and_doc, ComparingDicts, ComparingLists

import json

from bs4 import BeautifulSoup
        

def test_GetShortQuestionBlock():
    gt_info, doc = gt_and_doc('tests/Pages/yourist-online/GroundTruth/ShortQuestionBlock.json',
                              'tests/Pages/yourist-online/Docs/ShortQuestionBlock.html')
    gt_info = ' '.join(gt_info)
    gt_info = json.loads(gt_info)

    pl = ParserYuristOnline()
    extracted_info = pl.GetShortQuestionBlock(doc)

    assert all(ComparingDicts(gt_info, extracted_info))

def test_GetAnswerInformation():
    gt_info, doc = gt_and_doc('tests/Pages/yourist-online/GroundTruth/GetAnswerInformation.json',
                              'tests/Pages/yourist-online/Docs/GetAnswerInformation.html')
    gt_info = ' '.join(gt_info)
    gt_info = json.loads(gt_info)

    pl = ParserYuristOnline()
    extracted_info = pl.GetAnswerInformation(doc)

    assert all(ComparingDicts(gt_info, extracted_info))

def test_GetAllShortQuestions():
    gt_info, doc = gt_and_doc('tests/Pages/yourist-online/GroundTruth/GetAllShortQuestions.json',
                              'tests/Pages/yourist-online/Docs/GetAllShortQuestions.html', e2=None)
    gt_info = ' '.join(gt_info)
    gt_info = json.loads(gt_info)

    pl = ParserYuristOnline()
    extracted_info = pl.GetAllShortQuestions(doc)[:2]

    assert all(ComparingLists(gt_info, extracted_info))

def test_GetAllAnswers():
    pl = ParserYuristOnline()

    gt_info, doc = gt_and_doc('tests/Pages/yourist-online/GroundTruth/GetAllAnswers.json',
                              'tests/Pages/yourist-online/Docs/GetAllAnswers.html', e2=None)
    gt_info = ' '.join(gt_info)
    gt_info = json.loads(gt_info)

    extracted_info = pl.GetAllAnswers(doc)

    assert all(ComparingLists(gt_info, extracted_info))


if __name__ == '__main__':
    test_GetShortQuestionBlock()
    test_GetAnswerInformation()
    test_GetAllShortQuestions()
    test_GetAllAnswers()