

#calss header
class _STIFF():
	def __init__(self,): 
		self.name = "STIFF"
		self.definitions = [u'firm or hard: ', u'not easily bent or moved: ', u'If you are stiff or part of your body is stiff, your muscles hurt when they are moved: ', u'behaving in a way that is formal and not relaxed: ', u'severe and difficult: ', u'a strong wind', u'an alcoholic drink that is very strong: ', u'A stiff price is very expensive: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
