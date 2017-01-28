

#calss header
class _STRICT():
	def __init__(self,): 
		self.name = "STRICT"
		self.definitions = [u"strongly limiting someone's freedom to behave as they wish, or likely to severely punish someone if they do not obey: ", u'exactly correct: ', u'used to refer to someone who follows the rules and principles of a belief or way of living very carefully and exactly, or a belief or principle that is followed very carefully and exactly: ', u'in the most limited meaning of a word, phrase, etc.: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
