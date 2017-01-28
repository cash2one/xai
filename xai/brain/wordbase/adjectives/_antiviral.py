

#calss header
class _ANTIVIRAL():
	def __init__(self,): 
		self.name = "ANTIVIRAL"
		self.definitions = [u'An antiviral drug or treatment is used to cure an infection or disease caused by a virus: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
