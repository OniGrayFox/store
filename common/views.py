class TitleMixin:
    title = None

    def get_contex_data(self, **kwargs):
        context = super(TitleMixin, self).get_contex_data(**kwargs)
        context['title'] = self.title
        return context

