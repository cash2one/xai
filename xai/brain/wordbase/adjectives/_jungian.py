

#calss header
class _JUNGIAN():
	def __init__(self,): 
		self.name = "JUNGIAN"
		self.definitions = [u'of or connected with the ideas of the Swiss psychoanalyst Carl Gustav Jung: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
