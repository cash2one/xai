

#calss header
class _JARRING():
	def __init__(self,): 
		self.name = "JARRING"
		self.definitions = [u'a jarring sight, sound, or experience is so different or unexpected that it has a strong and unpleasant effect on something or someone: ', u'wrong or unsuitable: ', u'shaking or moving violently: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
