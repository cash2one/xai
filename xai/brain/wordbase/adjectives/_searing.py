

#calss header
class _SEARING():
	def __init__(self,): 
		self.name = "SEARING"
		self.definitions = [u'If something, such as a feeling or temperature, is described as searing, it is extreme: ', u'(especially of a criticism or story) very powerful and emotional or criticizing someone or something very strongly: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
