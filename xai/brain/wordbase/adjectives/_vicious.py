

#calss header
class _VICIOUS():
	def __init__(self,): 
		self.name = "VICIOUS"
		self.definitions = [u'Viscious people or actions show an intention or wish to hurt someone or something very badly: ', u'used to describe an object, condition, or remark that causes great physical or emotional pain: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
