

#calss header
class _HOW():
	def __init__(self,): 
		self.name = "HOW"
		self.definitions = [u'in what way, or by what methods: ', u"used to ask about someone's physical or emotional state: ", u'used in questions that ask what an experience or event was like: ', u'used for emphasis: ', u'used to emphasize that something is strange, stupid, etc.', u'used to ask someone if they are well and happy: ', u'used as greetings', u'used when you want someone to explain what they have just said: ', u'used when asking if something you have done for someone is satisfactory: ', u'used to show that you feel the same way as someone: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
