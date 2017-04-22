from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from django.utils.translation import ugettext, ugettext_lazy as _
from .models import Profile
from .forms import UserRegisterForm

class ProfileInline(admin.StackedInline):
    """ Profile user information. """
    model = Profile
    can_delete = False


class UserAdmin(admin.ModelAdmin):
    list_display = ('id','username', 'email', 'first_name', 'last_name','is_active'
        ,'get_balance', 'get_accaunt')
    list_select_related = ('user_information', )
    list_filter = ('is_active', 'groups')
    readonly_fields = ('date_joined','last_login')
    actions = ['activate']
    form = UserRegisterForm
    inlines = (ProfileInline, )

    def get_balance(self, instance):
        return instance.user_information.balance
    get_balance.short_description = 'Balance'

    def get_accaunt(self, instance):
        return instance.user_information.accaunt
    get_accaunt.short_description = 'account'


    def get_fieldsets(self, request, obj=None):
        """ 
        Set the permission field for managers only is_active, 
        for superuser the extended permission. 
        """
        
        if request.user.is_superuser:
            perm_fields = ('is_active', 'is_staff', 'is_superuser',
                           'groups', 'user_permissions')
        else:
            perm_fields = ('is_active',)

        return [(None, {'fields': ('username', 'password')}),
                (_('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
                (_('Permissions'), {'fields': perm_fields}),
                (_('Important dates'), {'fields': ('last_login', 'date_joined')})]


    def activate(self, request, queryset):        
        """Specific activities for approve user."""        
        queryset.update(is_active=True)
    activate.short_description = "Activate selected Users"


    def get_queryset(self, request):
        """ 
        Permission for managers to see only clients profile. 
        Deny viewing superuser and managers profile. 
        """
        qs = super(UserAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(is_superuser=False).filter(is_staff=False)


admin.site.unregister(User)
admin.site.register(User, UserAdmin)

