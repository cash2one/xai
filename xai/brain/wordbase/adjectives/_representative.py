

#calss header
class _REPRESENTATIVE():
	def __init__(self,): 
		self.name = "REPRESENTATIVE"
		self.definitions = [u'typical of, or the same as, others in a larger group of people or things: ', u'A representative system of government is one in which people vote for politicians to represent them.']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
