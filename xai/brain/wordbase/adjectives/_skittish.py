

#calss header
class _SKITTISH():
	def __init__(self,): 
		self.name = "SKITTISH"
		self.definitions = [u'(of people and animals) nervous or easily frightened: ', u'(of a person) not serious and likely to change their beliefs or opinions often: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
