

#calss header
class _PUBLIC():
	def __init__(self,): 
		self.name = "PUBLIC"
		self.definitions = [u'relating to or involving people in general, rather than being limited to a particular group of people: ', u'provided by the government from taxes to be available to everyone: ', u'A public place is one where a lot of people are: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
