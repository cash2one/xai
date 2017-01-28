

#calss header
class _CUNNING():
	def __init__(self,): 
		self.name = "CUNNING"
		self.definitions = [u'Cunning people are clever at planning something so that they get what they want, especially by tricking other people, or things that are cleverly made for a particular purpose: ', u'pretty and attractive: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
