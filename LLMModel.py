from ibm_watson_machine_learning.foundation_models.utils.enums import ModelTypes
from ibm_watson_machine_learning.metanames import GenTextParamsMetaNames as GenParams
from ibm_watson_machine_learning.foundation_models import Model
import prompt_template as pt

credentials= {"url":"https://us-south.ml.cloud.ibm.com","apikey":'lRBYRLWZgKwlP3Cq0OEyDgbdebD5gy97sUtmj52vJBqw'}
model_id = ModelTypes.FLAN_T5_XXL

parameters ={
    GenParams.MAX_NEW_TOKENS :20#Defining parameters for model .
}
model = Model(
    model_id=model_id,
    credentials=credentials,
    params=parameters,
    project_id='415cd205-351e-432a-bb2b-a9f749ffda75'
)#initializing FLAN_T5_XXL model for text classification.


def augment(template,content):

    """
    params:-
    template:- phrase the content of the given resume information into proper prompt for LLM model resume classification.
    content:-pandas dataframe with columns like Name,Email,Phone,Summary,Skills,Professional Experience,Education,Filename.
    """
    return template % (content["Summary"],content["Skills"],content["Professional Experience"])#this command will replace the first place holder %s with context



def categorize_resume_content(model ,resume_content):
    """
    params:-
    resume_content: pandas dataframe with columns like Name,Email,Phone,Summary,Skills,Professional Experience,Education,Filename.
    model: Model which is going to be used for the resume classsification.

    output:-
    category_: dictionary with keys "job_category" and "resume_associated" where job_category is the category of the resume_content passed and 
    """
    category_ = {"job_category":"" , "resume_associated":""}
    augmented_prompt = augment(pt.prompt_template, resume_content) # augument the csv resume content with proper prompt . 
    category = model.generate_text(prompt = augmented_prompt) 
    category_["job_category"]= category 
    category_["resume_associated"] = resume_content["Filename"] # adding the filename to the category dictionary.
    return category_


