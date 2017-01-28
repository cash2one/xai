

#calss header
class _INVOLUNTARY():
	def __init__(self,): 
		self.name = "INVOLUNTARY"
		self.definitions = [u'not done by choice; done unwillingly, or without the decision or intention of the person involved: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
