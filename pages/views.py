from django.shortcuts import render, HttpResponseRedirect
from django.http import Http404
from django.urls import reverse
from django.views.generic import TemplateView

import pickle
import pandas as pd


def homePageView(request):
    return render(request, "home.html", {
        "mynumbers": [1, 2, 3, 4, 5, 6],
        "firstName": "Noufil",
        "lastName": "Saqib",
    })


def homePost(request):
    choice = -999
    gmat = -999

    try:
        currChoice = request.POST["choice"]
        gmatStr = request.POST["gmat"]

        print("*** Years work experience: " + str(currChoice))
        choice = int(currChoice)
        gmat = float(gmatStr)
    except:
        return render(request, "home.html", {
            "error_message": "*** The data submitted is invalid. Please try again",
            "mynumbers": [1, 2, 3, 4, 5, 6],
        })
    else:
        return HttpResponseRedirect(reverse("results", kwargs={"choice": choice, "gmat": gmat},))


def results(request, choice, gmat):
    print("*** Inside results()")

    with open("/Users/noufi/Desktop/CST/Sem4/4949_BigDataAnalyticsMethods/LL_Codes/helloworld/model_pkl", "rb") as f:
        loadedModel = pickle.load(f)

    singleSampleDf = pd.DataFrame(columns=["gmat", "work_experience"])

    workExperience = float(choice)
    print("*** GMAT Score: " + str(gmat))
    print("*** Work Experience: " + str(workExperience))
    singleSampleDf = singleSampleDf._append({
        "gmat": gmat,
        "work_experience": workExperience,
    }, ignore_index=True)

    singlePrediction = loadedModel.predict(singleSampleDf)
    print("*** Prediction: " + str(singlePrediction))

    return render(request, "results.html", {
        "choice": workExperience,
        "gmat": gmat,
        "prediction": singlePrediction,
    })


def aboutPageView(request):
    return render(request, "about.html")


def noufilPageView(request):
    return render(request, "noufil.html")
