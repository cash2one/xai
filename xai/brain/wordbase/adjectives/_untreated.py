

#calss header
class _UNTREATED():
	def __init__(self,): 
		self.name = "UNTREATED"
		self.definitions = [u'An untreated substance is not cleaned and has not had special substances added to protect it or make it safe to use: ', u'Untreated illnesses, injuries, people, or animals do not receive medical treatment: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
