from django import forms
from models import Category, Project, ProjectUpdate, DonationLevel
from django.forms.models import inlineformset_factory
from models import Category, DonationLevel, Project
from datetime import datetime, timedelta
from datetime import date
from ckeditor.fields import RichTextField


class ProjectForm(forms.ModelForm):
    """
    Form used for the Create and Update Project View. Controls what fields
    the user can access and their basic appearance to the user.
    """
    # sets the lat and long fields to hidden (clicking on the map updates them)
    location_latitude = forms.DecimalField(initial=37.774929, required = False, widget=forms.HiddenInput())
    location_longitude = forms.DecimalField(initial=-122.419418, required = False, widget=forms.HiddenInput())
    # extra = forms.IntegerField(widget=forms.HiddenInput(attrs={'id':'id_extra'}))

    # generates options of categories and populates Multiple Choice field with options.
    options = [(category, category) for category in Category.valid_categories]
    categories_select = forms.MultipleChoiceField(choices=options, required=False, widget=forms.HiddenInput(), label='')

    subfund_payment = forms.CharField(initial=12, required= False)
    # date time
    today = datetime.today()
    enddate = today + timedelta(days=10)

    title = forms.CharField(label='Campaign Name', required=True)
    funding_goal = forms.DecimalField(label='Fundraising Goal',initial=3000, required=True)
    end_date = forms.DateField(label='Fundraising Deadline',initial=enddate, required=True, widget=forms.TextInput(attrs={'type': 'date','id':'date-picks'} ))
    tagline = forms.CharField(label='',required=False, widget=forms.HiddenInput())
    
    video_url = forms.URLField(initial='https://www.youtube.com/watch?v=fCrs2eASgFg', widget=forms.HiddenInput())

    org_name = forms.CharField(label='', initial='SSF', required=True, widget=forms.HiddenInput())

    impact_power = forms.FloatField(label='', initial=12345, required=False, widget=forms.HiddenInput())
    total_kwh_value = forms.DecimalField(label='', initial=12345, required=False, widget=forms.HiddenInput())

    org_start_date = forms.DateField(label='',initial=today, required=False)
    
    org_about = forms.CharField(label='', initial='<p> Solar is a simple solution to help reduce carbon emissions, make the air cleaner, and strengthen communities. </p> <p> Every dollar donated to the Solar Seed Fund is invested directly into community-serving nonprofit solar projects, like schools, homeless shelters, and food pantries.</p> <p> When these nonprofits go solar, they not only save money, but re-allocate money spent on dirty energy toward fulfilling their missions. That means that your donated dollar helps both people and the planet. We call that a win-win. </p> <p> When each project is complete, RE-volv will send you the address and photos of the community benefiting from your donation.</p>  <p> Learn more about the Solar Seed Fund by watching the video below. </p>' , required= False, widget=forms.Textarea )

    location = forms.CharField(label='', initial='San Francisco',  required=False, widget=forms.HiddenInput())

    project_url = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': '(project url)'}))

    cover_photo = forms.ImageField(required=True)

    class Meta:
        model = Project
        # fields that need to be filled out
        localized_fields = ('__all__')

        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'e.g. Other Avenues Food Cooperative'}),
            'subfund_payment': forms.TextInput(attrs={'placeholder': 'e.g. Sub fundraise'}),
            'tagline': forms.TextInput(attrs={'placeholder': 'e.g. Power the future!'}),
            'funding_goal': forms.TextInput(attrs={'placeholder': 'e.g. $1000', 'min_value': 0, 'decimal_places': 2}),
            'project_url': forms.TextInput(attrs={'placeholder': 'e.g. PowerCommunityDanceStudio2'}),
            'impact_power': forms.NumberInput(attrs={'placeholder': 'e.g. 12.0'}),
            'end_date': forms.DateInput(attrs={'placeholder': 'e.g. 10/25/2006', 'input_formats': '%m/%d/%Y'}),
            'video_url': forms.URLInput(attrs={'placeholder': 'e.g. youtube.com/url_to_video'}),
            'org_name': forms.TextInput(attrs={'placeholder': 'e.g. Other Avenues'}),
            'org_start_date': forms.DateInput(attrs={'placeholder': 'e.g. 10/25/2006', 'input_formats': '%m/%d/%Y'}),
            'org_about': forms.Textarea(attrs={
                'placeholder': 'e.g. Other Avenues is a worker-owned cooperative that seeks to maintain a thriving business while providing food and supplies for sustainable living, supporting organic and local farms and to serve as a model of workplace democracy for the community.'}),
            'location': forms.TextInput(attrs={'placeholder': 'e.g. 3930 Judah Street San Francisco, CA 94122'}),
            'description': forms.Textarea(attrs={
                'placeholder': "e.g. The solar energy system will be a 36kW project that provides 33% of Other Avenue's electricity needs."}),
            'people_affected': forms.NumberInput(attrs={'placeholder': 'e.g. 12'}),
            # 'actual_energy': forms.TextInput(attrs={'placeholder': 'e.g. 10000', 'min_value': 0, 'decimal_places': 2}),
            'total_kwh_value': forms.NumberInput(attrs={'placeholder': 'e.g. 50000'}),
        }

        fields = (
            'title',
            'tagline',
            'subfund_payment',
            'funding_goal',
            'impact_power',
            'end_date',
            'video_url',
            'cover_photo',
            'profile_picture',
            'org_name',
            'org_about',
            'org_start_date',
            'location',
            'location_latitude',
            'location_longitude',
            'categories_select',
            'description',
            'people_affected',
            # 'actual_energy',
            'total_kwh_value',
            'project_url'
        )
        labels = {
            'cover_photo':'Cover Photo',
            'profile_picture':'Profile Photo',
            'people_affected' : '',
            'location' : ''
        }

    def clean_categories_select(self):
        """ This method processes the input from the hidden categories list field, which
        is a string of the comma separated values. It parses it and insures all the categories
        are valid, then converts it into an actual list.
        """
        data = self.cleaned_data['categories_select']
        categories_select = filter(None, data)
        # checks if a/ll the categories in it are valid
        for category in categories_select:
            if category not in Category.valid_categories:
                raise forms.ValidationError("You have entered an invalid category.")
        return categories_select

class ProjectSubForm(forms.ModelForm):
    """
    Form used for the Create and Update Project View. Controls what fields
    the user can access and their basic appearance to the user.
    """
    # sets the lat and long fields to hidden (clicking on the map updates them)
    location_latitude = forms.DecimalField(initial=37.774929, required = False, widget=forms.HiddenInput())
    location_longitude = forms.DecimalField(initial=-122.419418, required = False, widget=forms.HiddenInput())
    # extra = forms.IntegerField(widget=forms.HiddenInput(attrs={'id':'id_extra'}))

    # generates options of categories and populates Multiple Choice field with options.
    options = [(category, category) for category in Category.valid_categories]
    categories_select = forms.MultipleChoiceField(choices=options, required=False, widget=forms.HiddenInput(), label='')

    subfund_payment = forms.ChoiceField(choices=Project.objects.get_active_fundraiser().values_list('id','title'), required= False)
    # date time
    today = datetime.today()
    enddate = today + timedelta(days=10)

    title = forms.CharField(label='Campaign Name', required=True)
    funding_goal = forms.DecimalField(label='Fundraising Goal', initial=100, required=True)
    end_date = forms.DateField(label='Fundraising Deadline',initial=enddate, required=True, widget=forms.TextInput(attrs={'type': 'date','id':'date-picks'} ))

    tagline = forms.CharField(label='',required=False, widget=forms.HiddenInput())
    
    video_url = forms.URLField(initial='https://www.youtube.com/watch?v=fCrs2eASgFg', widget=forms.HiddenInput())

    org_name = forms.CharField(label='', initial='SUBSF', required=True, widget=forms.HiddenInput())

    impact_power = forms.FloatField(label='', initial=12345, required=False, widget=forms.HiddenInput())
    total_kwh_value = forms.DecimalField(label='', initial=12345, required=False, widget=forms.HiddenInput())

    org_start_date = forms.DateField(label='',initial=today, required=False)
    
    org_about = forms.CharField(label='', initial='Solar is a simple solution to help reduce carbon emissions, make the air cleaner, and strengthen communities.<br> I started this fundraiser to help bring the benefits of clean energy to communities that need it most. Every dollar donated to this campaign is invested directly into a community-serving nonprofit solar project, like schools, homeless shelters, and food pantries. <br> When these nonprofits go solar, they not only save money, but re-allocate money spent on dirty energy toward fulfilling their missions. That means that your donated dollar helps both people and the planet. We call that a win-win. <br> When each project is complete, RE-volv will send you the address and photos of the community benefiting from your donation. <br> <strong> Please donate to my campaign, every little bit helps.  </strong>' , required= False, widget=forms.Textarea )

    location = forms.CharField(label='', initial='San Francisco',  required=False, widget=forms.HiddenInput())

    project_url = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': '(project url)'}))

    profile_picture = forms.ImageField(required=True)

    class Meta:
        model = Project
        # fields that need to be filled out
        localized_fields = ('__all__')

        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'e.g. Other Avenues Food Cooperative'}),
            'subfund_payment': forms.TextInput(attrs={'placeholder': 'e.g. Sub fundraise'}),
            'tagline': forms.TextInput(attrs={'placeholder': 'e.g. Power the future!'}),
            'funding_goal': forms.TextInput(attrs={'placeholder': 'e.g. $1000', 'min_value': 0, 'decimal_places': 2}),
            'project_url': forms.TextInput(attrs={'placeholder': 'e.g. PowerCommunityDanceStudio2'}),
            'impact_power': forms.NumberInput(attrs={'placeholder': 'e.g. 12.0'}),
            'end_date': forms.DateInput(attrs={'placeholder': 'e.g. 10/25/2006', 'input_formats': '%m/%d/%Y'}),
            'video_url': forms.URLInput(attrs={'placeholder': 'e.g. youtube.com/url_to_video'}),
            'org_name': forms.TextInput(attrs={'placeholder': 'e.g. Other Avenues'}),
            'org_start_date': forms.DateInput(attrs={'placeholder': 'e.g. 10/25/2006', 'input_formats': '%m/%d/%Y'}),
            'org_about': forms.Textarea(attrs={
                'placeholder': 'e.g. Other Avenues is a worker-owned cooperative that seeks to maintain a thriving business while providing food and supplies for sustainable living, supporting organic and local farms and to serve as a model of workplace democracy for the community.'}),
            'location': forms.TextInput(attrs={'placeholder': 'e.g. 3930 Judah Street San Francisco, CA 94122'}),
            'description': forms.Textarea(attrs={
                'placeholder': "e.g. The solar energy system will be a 36kW project that provides 33% of Other Avenue's electricity needs."}),
            'people_affected': forms.NumberInput(attrs={'placeholder': 'e.g. 12'}),
            # 'actual_energy': forms.TextInput(attrs={'placeholder': 'e.g. 10000', 'min_value': 0, 'decimal_places': 2}),
            'total_kwh_value': forms.NumberInput(attrs={'placeholder': 'e.g. 50000'}),
        }

        fields = (
            'title',
            'tagline',
            'subfund_payment',
            'funding_goal',
            'impact_power',
            'end_date',
            'video_url',
            'cover_photo',
            'profile_picture',
            'org_name',
            'org_about',
            'org_start_date',
            'location',
            'location_latitude',
            'location_longitude',
            'categories_select',
            'description',
            'people_affected',
            # 'actual_energy',
            'total_kwh_value',
            'project_url'
        )
        labels = {
            'cover_photo':'Cover Photo',
            'profile_picture':'Profile Photo',
            'people_affected' : '',
            'location' : ''
        }

    def clean_categories_select(self):
        """ This method processes the input from the hidden categories list field, which
        is a string of the comma separated values. It parses it and insures all the categories
        are valid, then converts it into an actual list.
        """
        data = self.cleaned_data['categories_select']
        categories_select = filter(None, data)
        # checks if a/ll the categories in it are valid
        for category in categories_select:
            if category not in Category.valid_categories:
                raise forms.ValidationError("You have entered an invalid category.")
        return categories_select

class ProjectStatusForm(forms.ModelForm):
    """
    An empty form, used so that one can update the project status through
    the ReviewProjectView
    """

    class Meta:
        model = Project
        # fields that need to be filled out, empty on purpose
        fields = ()


class EditProjectUpdateForm(forms.ModelForm):
    """
    A form used to edit updates about a project
    """

    class Meta:
        model = ProjectUpdate

        widgets = {
            'update_text': forms.Textarea(attrs={
                'placeholder': 'e.g. Thank you for all the support! The project has been going extremely well. These are the milestones we have hit so far, and this is what we plan to do in the near future.'}),
        }

        fields = (
            'update_text',
        )


def make_donation_level_formset(extra):
    ProjectDonationLevelFormSet = inlineformset_factory(Project, DonationLevel, extra=extra)
    return ProjectDonationLevelFormSet
