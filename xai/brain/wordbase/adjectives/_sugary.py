

#calss header
class _SUGARY():
	def __init__(self,): 
		self.name = "SUGARY"
		self.definitions = [u'containing sugar: ', u'too good or kind or expressing feelings of love in a way that is not sincere: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
