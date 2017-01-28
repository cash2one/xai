

#calss header
class _IMPENITENT():
	def __init__(self,): 
		self.name = "IMPENITENT"
		self.definitions = [u'not sorry or ashamed about something bad you have done: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
