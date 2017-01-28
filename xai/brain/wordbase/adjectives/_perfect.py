

#calss header
class _PERFECT():
	def __init__(self,): 
		self.name = "PERFECT"
		self.definitions = [u'complete and correct in every way, of the best possible type or without fault: ', u'used to emphasize a noun: ', u'exactly right for someone or something: ', u'of or relating to a verb indicating a completed action: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
