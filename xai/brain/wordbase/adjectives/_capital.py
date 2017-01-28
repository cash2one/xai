

#calss header
class _CAPITAL():
	def __init__(self,): 
		self.name = "CAPITAL"
		self.definitions = [u'(of a letter of the alphabet) in the form and larger size that is used at the beginning of sentences and names: ', u'a crime that can be punished by death: ', u'very good or excellent: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
