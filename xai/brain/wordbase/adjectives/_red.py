

#calss header
class _RED():
	def __init__(self,): 
		self.name = "RED"
		self.definitions = [u'of the colour of fresh blood: ', u'used to describe hair that is an orange-brown colour', u'If you go/turn red, your face becomes red because you are angry or embarrassed: ', u'If your eyes are red, the white part of your eyes and the skin around your eyes is red, because of crying, tiredness, too much alcohol, etc.']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
